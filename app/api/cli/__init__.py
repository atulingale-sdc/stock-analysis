import asyncio
import sys
import typer
import inject

from app.settings import Settings
from app.service.stock_analysis import StockAnalysisService


cli = typer.Typer()


def start_cli():
    # Bootstrap
    service = StockAnalysisService()
    print("Enter query to analyze stock:")
    for line in sys.stdin:
        inp = line.rstrip()
        if 'exit' == inp.lower():
            break
        loop = asyncio.get_event_loop()
        loop.run_until_complete(service.analyse_user_query(inp))
        print("-------------------------------")
        print("-------------------------------")
        print("\nEnter query to analyze stock:")


@cli.command(name="start")
def start():
    conf = inject.instance(Settings)
    if conf.run_mode == 'CLI':
        start_cli()

