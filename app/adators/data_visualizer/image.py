import inject
import matplotlib.pyplot as plt
from datetime import date, datetime
from typing import Any
from app.settings import Settings
from app.adators.data_visualizer.base import Visualizer
from uuid import uuid4


class ImageVisualizer(Visualizer):
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

        plt.figure(figsize=(8, 5))
        plt.plot(dates, high, marker='o', linestyle='-', color='b')
        plt.plot(dates, low, marker='o', linestyle='-.', color='r', label='High')
        plt.plot(dates, open_, marker='o', linestyle=':', color='g', label='Open')
        plt.plot(dates, close_, marker='o', linestyle='--', color='y', label='Close')
        # plt.plot(dates, volume, marker='o', linestyle='-', color='c', label='Volume')
        # Adding legend
        plt.legend(loc='upper left')

        # Adding titles and labels
        plt.title(f'Stock Details {group_by.title()}ly for period {period}')
        plt.xlabel(group_by.title())

        # Displaying the plot
        plt.grid(True)
        graph_name = f"images/{uuid4()}.png"
        plt.savefig(graph_name)
        return graph_name
