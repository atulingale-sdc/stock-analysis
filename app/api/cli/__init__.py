import asyncio
import sys
import typer
import inject

from app.settings import Settings
from app.service.stock_analysis import StockAnalysisService


cli = typer.Typer()


async def call_service():
    service = StockAnalysisService()
    print("Enter query to analyze stock:")
    for line in sys.stdin:
        inp = line.rstrip()
        if 'exit' == inp.lower():
            break

        summery, image = await service.analyse_user_query(inp)
        print(summery)
        print("-------------------------------")
        print("-------------------------------")
        print("\nEnter query to analyze stock:")


def start_cli():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(call_service())


@cli.command(name="start")
def start():
    conf = inject.instance(Settings)
    if conf.run_mode == 'CLI':
        start_cli()
    else:
        import uvicorn
        uvicorn.run(
            "app.bootstrap.server:api",
            host=conf.app_host,
            port=conf.app_port,
            reload=conf.can_reload,
        )
