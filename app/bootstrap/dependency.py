import logging
from functools import lru_cache

import inject
from app.core.settings import CoreSettings
from app.settings import Settings
from app.adators.llm.base import LLMAdaptor
from app.adators.llm.openai import OpenAIAdaptor
from app.adators.data_api.base import DataAPIAdaptor
from app.adators.data_api.polygon_io import PolygonIoAdapter
from app.adators.data_visualizer.base import Visualizer
from app.adators.data_visualizer.terminal import TerminalVisualizer

logger = logging.getLogger(__name__)


@lru_cache
def get_settings() -> Settings:
    return Settings()


@lru_cache
def get_llm_model() -> LLMAdaptor:
    settings = get_settings()
    return OpenAIAdaptor(conf=settings)


@lru_cache
def get_data_api_provider() -> DataAPIAdaptor:
    settings = get_settings()
    return PolygonIoAdapter(conf=settings)


@lru_cache
def get_data_visualiser() -> Visualizer:
    settings = get_settings()
    if settings.run_mode == 'CLI':
        return TerminalVisualizer(conf=settings)


def configure_dependency(binder: inject.Binder) -> None:
    """
    Configure dependency injection container

    :param binder:
    :return:
    """
    binder.bind(CoreSettings, get_settings())
    binder.bind(Settings, get_settings())
    binder.bind(LLMAdaptor, get_llm_model())
    binder.bind(DataAPIAdaptor, get_data_api_provider())
    binder.bind(Visualizer, get_data_visualiser())
