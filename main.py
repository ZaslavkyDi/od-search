from api_handler import OrderfulApiHandler
from models.pagination import PaginationQueryFilter

if __name__ == '__main__':
    api = OrderfulApiHandler()
    r = api.get_transactions(
        pagination=PaginationQueryFilter(
            limit=10,
        )
    )
