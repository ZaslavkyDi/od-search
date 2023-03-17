from typing import Any

import requests
from requests import Response

from app.config import get_orderful_settings
from app.models.api_handler.orderful.request import TransactionQueryFilter
from app.models.api_handler.orderful.response import TransactionsResponse
from app.models.pagination import PaginationQueryFilter


class OrderfulApiHandler:
    def __init__(self):
        self._orderful_settings = get_orderful_settings()

    def get_transactions(
        self,
        pagination: PaginationQueryFilter,
        query_filter: TransactionQueryFilter | None = None,
        next_page_url: str | None = None,
    ) -> TransactionsResponse:
        params: dict[str, Any] = {}
        url: str = self._orderful_settings.transaction_url

        if next_page_url:
            url = next_page_url
        elif query_filter:
            params.update(query_filter.to_request_not_none_query_format())
            params.update(pagination.to_request_query_format())
        else:
            params.update(pagination.to_request_query_format())

        response: Response = requests.get(
            url=url,
            headers=self._orderful_settings.orderful_auth_header,
            params=params,
        )
        response.raise_for_status()

        return TransactionsResponse(**response.json())
