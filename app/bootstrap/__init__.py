import typing
import os

import inject
from app.core.settings import CoreSettings
from app.settings import Settings
from app.core.logger import setup_logging

from .dependency import configure_dependency


def boot():
    # Configure the Dependencies for the Application
    inject.configure(configure_dependency)
    # First setup logging
    setup_logging()

    # Return CLI Application
    from app.api.cli import cli
    return cli
