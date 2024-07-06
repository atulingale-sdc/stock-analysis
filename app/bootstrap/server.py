import inject
from app.settings import Settings
from app.core.bootstrap import create_app

from .dependency import configure_dependency

# Configure the Dependencies for the Application
inject.configure(configure_dependency)


def init_app():
    from app.api import login as auth

    settings = inject.instance(Settings)
    api_ = create_app(settings)
    return api_


# Create the FAST API app
api = init_app()
