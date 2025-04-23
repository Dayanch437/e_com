from rest_framework import routers

from api.store.viewsets import ProductViewSet, CategoryViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns = router.urls