from typing import Any
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from abc import ABC, abstractmethod


class Visualizer(ABC):

    @abstractmethod
    async def plot_bar_chart(
            self,
            data: Any, period: str, group_by: str, start: datetime | date, end: datetime | date
    ):
        raise NotImplementedError()

    @staticmethod
    def get_labels_for_period(start: datetime | date, end: datetime | date, group_by: str):
        labels = []
        temp_ = start
        while temp_ <= end:
            if group_by == 'year':
                labels.append(temp_.strftime("%Y"))
                temp_ = temp_ + relativedelta(years=1)
            elif group_by == 'month':
                labels.append(temp_.strftime("%b-%Y"))
                temp_ = temp_ + relativedelta(months=1)
            elif group_by == 'quarter':
                raise NotImplementedError("Logic is not implemented for Quarterly grouping")
            elif group_by == 'week':
                raise NotImplementedError("Logic is not implemented for Weekly grouping")
            elif group_by == 'day':
                labels.append(temp_.strftime("%d-%b-%Y"))
                temp_ = temp_ + relativedelta(days=1)
            elif group_by == 'hour':
                labels.append(temp_.strftime("%h:%m"))
                temp_ = temp_ + relativedelta(hours=1)
            else:
                # For minutes and hours
                labels.append(temp_.strftime("%h:%m:%s"))
                temp_ = temp_ + relativedelta(seconds=1)

        return labels
