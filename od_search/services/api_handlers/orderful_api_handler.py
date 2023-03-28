from typing import Any
from urllib.parse import urljoin

import requests
from requests import Response

from od_search.config import get_orderful_settings
from od_search.models.api_handler.orderful.request import TransactionQueryFilter
from od_search.models.api_handler.orderful.response import (
    TransactionsResponse,
    TransactionX12AttachmentResponse,
)
from od_search.models.pagination import PaginationQueryFilter


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

    def get_x12_transaction_format(self, transaction_id: int) -> TransactionX12AttachmentResponse:
        url: str = self._orderful_settings.transaction_url

        attachments_url: str = urljoin(url, f"{transaction_id}/attachments")
        response: Response = requests.get(
            url=attachments_url,
            headers=self._orderful_settings.orderful_auth_header,
        )
        response.raise_for_status()

        payload: list[dict[str, Any]] = response.json()
        x12_format: list[dict[str, Any]] = [i for i in payload if i["format"] == "x12"]

        if len(x12_format) == 0:
            raise ValueError(f"Can not find X12 format by {attachments_url}: {payload}")

        return TransactionX12AttachmentResponse(**x12_format[0])
