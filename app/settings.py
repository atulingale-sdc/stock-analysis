from app import __about__
from app.core.settings import CoreSettings


class Settings(CoreSettings):
    """ """

    app_title: str = __about__.__NAME__
    app_version: str = __about__.__VERSION__
    api_version: str = __about__.__API_VERSION__
    app_description: str = __about__.__DESCRIPTION__
