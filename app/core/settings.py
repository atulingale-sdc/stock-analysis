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

    app_port: int = 8080
    app_host: str = "127.0.0.1"
    app_base_url: str | None = None
    base_url: str | None = None
    root_path: str = ""
    openapi_url: str = "/openapi.json"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    token_url: str = "token"
    shared_secret_key: str | None = None
    app_secret_key: str | None = None

    force_https: bool = False
    cors_origins: set[str] = {"http://127.0.0.1:8888", "http://127.0.0.1:3000"}

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

    @property
    def can_reload(self) -> bool:
        """Determines if service can be reloaded on file change."""
        return self.is_local or self.is_dev
