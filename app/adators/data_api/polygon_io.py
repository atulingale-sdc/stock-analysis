from datetime import datetime, date

import inject

from polygon import RESTClient
from polygon.rest.models.aggs import Agg

from app.adators.data_api.base import DataAPIAdaptor
from app.settings import Settings


class PolygonIoAdapter(DataAPIAdaptor):

    @inject.autoparams('conf')
    def __init__(self, conf: Settings):
        if not conf.polygon_api_key:
            raise RuntimeError("Polygon API Key is not configured.")

        self.client = RESTClient(api_key=conf.polygon_api_key)

    async def get_aggregated_data(
            self, symbol: str, start: datetime | date, end: datetime | date,
            group_by: str
    ) -> list[Agg]:
        resp = self.client.get_aggs(
            ticker=symbol,
            multiplier=1,
            timespan=group_by,
            from_=start,
            to=end
        )
        return resp

