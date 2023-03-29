from typing import Dict, Any

from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    version: str = "0.1.0"
    host: str = "0.0.0.0"

    class Config:
        env_prefix = "app_"


class OrderfulSettings(BaseSettings):
    default_number_transaction_per_page: int = Field(
        100, exmple=100, description="How many transaction Orderful return in as a response."
    )
    api_key: str = Field(
        "set-up-your-api-key",
        example="dasfTfasfIhfasfnkndAsdsdaFASfafsfa",
        description="API Key for interacting with an Orderful platform.",
    )
    transaction_url: str = Field(
        "https://api.orderful.com/v2/transactions/",
        description="URL for getting Orderful transactions data.",
    )

    class Config:
        env_prefix = "orderful_"

    @property
    def orderful_api_key_header(self) -> str:
        return "orderful-api-key"

    @property
    def orderful_auth_header(self) -> Dict[str, Any]:
        return {
            self.orderful_api_key_header: self.api_key,
        }
