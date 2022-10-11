from app.services.api_handlers.orderful_api_handler import OrderfulApiHandler
from app.models import PaginationQueryFilter

if __name__ == '__main__':
    api = OrderfulApiHandler()
    r = api.get_transactions(
        pagination=PaginationQueryFilter(
            limit=10,
        )
    )
