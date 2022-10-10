import requests

from api_handler import OrderfulApiHandler
from constants import TransactionTypeId, TransactionDirection
from models.api_handler.orderful.request import TransactionQueryFilter
from models.pagination import PaginationQueryFilter

url = "https://api.orderful.com/v2/transactions/?limit=100&offset=0"

payload = {}
headers = {
    'orderful-api-key': 'xiwXH8EvftagxyyDLEeDA9b0E3gfiMsq5e88f8lR'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

if __name__ == '__main__':
    api = OrderfulApiHandler()
    r = api.get_transactions(
        pagination=PaginationQueryFilter(
            limit=10,
        )
    )

print()
