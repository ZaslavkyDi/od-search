from functools import lru_cache

from app.config.settings import OrderfulSettings


@lru_cache
def get_orderful_settings() -> OrderfulSettings:
    return OrderfulSettings()