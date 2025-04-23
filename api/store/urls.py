from rest_framework import routers

from api.store.viewsets import ProductViewSet, CategoryViewSet, CommentViewSet, SliderViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'sliders', SliderViewSet)
urlpatterns = router.urls