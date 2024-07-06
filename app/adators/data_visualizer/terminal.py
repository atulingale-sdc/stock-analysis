import inject
import plotext as plt
from datetime import date, datetime
from typing import Any
from app.settings import Settings
from app.adators.data_visualizer.base import Visualizer


class TerminalVisualizer(Visualizer):
    """Show charts on terminal."""

    @inject.autoparams('conf')
    def __init__(self, conf: Settings):
        self.conf = conf

    async def plot_bar_chart(
            self,
            data: Any, period: str, group_by: str, start: datetime | date, end: datetime | date
    ):
        """
        Prepare chart data and plots the chart.

        :param data:
        :param period:
        :param group_by:
        :param start:
        :param end:
        :return:
        """
        dates = self.get_labels_for_period(start=start, end=end, group_by=group_by)
        high, low, open_, close_, volume = [], [], [], [], []

        for item in data:
            high.append(item.high)
            low.append(item.open)
            open_.append(item.open)
            close_.append(item.close)
            volume.append(item.volume)

        plt.multiple_bar(
            dates,
            [high, low, open_, close_],
            label=["high", "low", "open", "close"]
        )
        plt.title(f"Stock Details {group_by.title()}ly for period {period}")
        plt.show()
