from rest_framework import routers
from .api import EmbarqueViewSet

router = routers.DefaultRouter()
router.register(r'embarques', EmbarqueViewSet, "embarques")

urlpatterns = router.urls