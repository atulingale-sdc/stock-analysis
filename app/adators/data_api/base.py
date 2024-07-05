from abc import abstractmethod, ABC
from datetime import datetime, date
from typing import Any


class DataAPIAdaptor(ABC):

    @abstractmethod
    async def get_aggregated_data(
            self, symbol: str, start: datetime | date, end: datetime | date, group_by: str
    ) -> list[Any]:

        raise NotImplemented
