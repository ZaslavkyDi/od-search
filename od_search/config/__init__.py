from functools import lru_cache

from od_search.config.settings import AppSettings, OrderfulSettings


@lru_cache
def get_orderful_settings() -> OrderfulSettings:
    return OrderfulSettings()


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()
