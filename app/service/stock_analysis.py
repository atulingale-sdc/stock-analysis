import logging

import inject
from datetime import datetime
from app.adators.llm.base import LLMAdaptor
from app.adators.data_api.base import DataAPIAdaptor
from app.adators.data_visualizer.base import Visualizer
from app.settings import Settings

logger = logging.getLogger(__name__)


class StockAnalysisService:
    """Provides high level interface for user interaction with application."""

    @inject.autoparams("conf", "llm_model", "data_api", "visual")
    def __init__(self, conf: Settings, llm_model: LLMAdaptor, data_api: DataAPIAdaptor, visual: Visualizer):
        """
        Initialize Service object with all required dependencies
        """
        self.llm = llm_model
        self.data_api = data_api
        self.visualizer = visual
        self.conf = conf

        self.symbol_map = {
            'APPLE': 'AAPL',
        }

    async def analyse_user_query(self, user_inp: str) -> tuple[str, str] | None:
        """
        Perform action on the user query and generate the requested output.
        :param user_inp: User query to work on.
        :return: Output of analysis or None
        """
        logger.info(f"Uer query: {user_inp}")
        data = await self.llm.extract_tokens(user_inp)
        logger.debug(f"Tokens: {data}")
        org = data.get("Organization") or ""
        symbol = self.symbol_map.get(org.upper())
        if not symbol:
            raise RuntimeError(f"Unable to find symbol for {org} to get stock information. Only 'Apple' is supported.")

        period = data.get("Period") | {}
        if not period:
            raise RuntimeError(f"No period provided to analyze the stock for {org}")

        # Find the best suitable groping clause in order to have the less data
        start_date = datetime.strptime(period.get("start_date"), "%Y-%m-%d")
        end_date = datetime.strptime(period.get("end_date"), "%Y-%m-%d")
        diff = (end_date - start_date)
        if diff.days > 365:
            group_by = "year"
        elif diff.days > 180:
            # Quarterly is not supported currently in graph generation
            # group_by = "quarter"
            group_by = "month"
        elif diff.days > 60:
            group_by = "month"
        elif diff.days > 15:
            # Weekly is not supported currently in graph generation
            # group_by = "week"
            group_by = "day"
        elif diff.days > 7:
            group_by = "day"
        elif diff.seconds > (120*60):
            group_by = "hour"
        elif diff.seconds > 120:
            group_by = "minute"
        else:
            group_by = "second"

        logger.info(f"Finding stock data for {symbol}, {start_date}, {end_date}, {group_by}")
        resp = await self.data_api.get_aggregated_data(symbol=symbol, start=start_date, end=end_date, group_by=group_by)
        logger.debug(f"Stock list: {resp}")
        data = [f"{symbol} ({org})"]
        for ag in resp:
            data.append(
                f"- Open: {ag.open}\n"
                f"- High: {ag.high}\n"
                f"- Low: {ag.low}\n"
                f"- Close: {ag.close}\n"
                f"- Volume: {ag.volume}\n"
            )
        logger.debug(f"Stock data: {data}")
        summery = await self.llm.create_summery(data="\n".join(data), period=f"{start_date} to {end_date}")
        logger.info(f"Summery: {summery}")

        # Plot the Graph with given data
        image = await self.visualizer.plot_bar_chart(
            data=resp, period=f"{start_date} to {end_date}", group_by=group_by, start=start_date, end=end_date
        )
        return summery, f"{self.conf.app_base_url}/{image}"
