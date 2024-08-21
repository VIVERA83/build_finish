from core.app import Application
from product.views import category_route, brand_route


def setup_routes(app: Application):
    """Настройка Роутов приложения."""
    app.include_router(category_route)
    app.include_router(brand_route)

