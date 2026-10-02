from pydantic import AliasChoices
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


ROOT_PATH = Path(__file__).resolve().parents[3]


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_PATH / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

class ModelSettings(Config):


    nvidia_model: str = Field(default="", validation_alias=AliasChoices(
        "NVIDIA_MODEL",
        "nvidia_model"
    ))
    nvidia_api_key: str = Field(default="", validation_alias=AliasChoices(
        "NVIDIA_API_KEY",
        "nvidia_api_key"
    ))
    nvidia_base_url:str = Field(default="", validation_alias=AliasChoices(
        "NVIDIA_BASE_URL",
        "nvidia_base_url"
    ))
    nvidia_vision_model:str = Field(default="", validation_alias=AliasChoices(
        "NVIDIA_VISION_MODEL",
        "nvidia_vision_model"
    ))


class Settings(ModelSettings):
    pass



settings = Settings()