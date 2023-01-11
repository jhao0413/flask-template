import toml
from pydantic import BaseModel
from pathlib import Path


class TomlSettings(BaseModel):
    """
    Toml配置文件帮助类
    """

    def __init__(self, toml_file_path: str) -> None:
        toml_file = Path(toml_file_path).absolute()
        if toml_file.is_file():
            toml_data = toml.load(toml_file)
            super().__init__(**toml_data)
        else:
            raise Exception(f"config file [{toml_file}] not found")


class DatabaseSetting(BaseModel):
    """数据库配置"""

    driver: str = "postgresql+psycopg2"
    host: str = "127.0.0.1"
    port: int = 5432
    database: str = "postgres"
    user: str = "postgres"
    password: str = "postgres"
    pool_size: int = 50
    track_modifications: bool = True

    @property
    def database_uri(self) -> str:
        """
        组装数据库uri
        :return:
        """
        return (
            f"{self.driver}://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )


class FlaskSettings(TomlSettings):
    """
    Flask设置
    """

    def __init__(self, toml_file_path: str):
        super().__init__(toml_file_path=toml_file_path)

    log_level: str = "DEBUG"
    secret_key: str = "654321"
    proxy_allow_frontend: list = ["127.0.0.1", "::1"]
    session_timeout: int = 86400
    app_name: str

    db: DatabaseSetting = DatabaseSetting()
