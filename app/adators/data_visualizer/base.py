from typing import Any
from datetime import datetime, date
from abc import ABC, abstractmethod


class Visualizer(ABC):

    @abstractmethod
    async def plot_bar_chart(
            self,
            data: Any, period: str, group_by: str, start: datetime | date, end: datetime | date
    ):
        raise NotImplementedError()
