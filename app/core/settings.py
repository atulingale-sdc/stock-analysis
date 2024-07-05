from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class CoreSettings(BaseSettings):
    """ """

    app_title: str
    app_version: str
    app_description: str

    app_env: str = "LOCAL"
    log_file: str = "app.log"
    run_mode: str = "CLI"
    log_level: str = "DEBUG"

    openai_api_key: str | None = None
    polygon_api_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def is_local(self) -> bool:
        """Returns True if the current environment is LOCAL."""
        return self.app_env == "LOCAL"

    @property
    def is_dev(self) -> bool:
        """Returns TRue if current Environment is DEV."""
        return self.app_env == "DEV"

    @property
    def is_prod(self) -> bool:
        """Returns tru if the current environment is PROD"""
        return self.app_env == "PROD"
