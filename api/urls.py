from django.urls import path, include
from .store.viewsets import latest_product_view
urlpatterns = [
    path("users/",include("api.user.urls")),
    path('auth/', include("api.auth.urls")),
    path('store/', include("api.store.urls")),
    path('cart/', include("api.cart.urls")),
    path("latest-products",latest_product_view),
]

