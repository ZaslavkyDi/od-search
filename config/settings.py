from typing import Dict, Any

from pydantic import BaseSettings, Field


class OrderfulSettings(BaseSettings):
    api_key: str = Field(
        example="dasfTfasfIhfasfnkndAsdsdaFASfafsfa",
        description="API Key for interacting with an Orderful platform."
    )
    transaction_url: str = Field(
        "https://api.orderful.com/v2/transactions/",
        description="URL for getting Orderful transactions data."
    )

    class Config:
        env_prefix = 'orderful_'

    @property
    def orderful_api_key_header(self) -> str:
        return "orderful-api-key"

    @property
    def orderful_auth_header(self) -> Dict[str, Any]:
        return {
            self.orderful_api_key_header: self.api_key,
        }
