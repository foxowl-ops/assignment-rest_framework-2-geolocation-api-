from django.urls import path, include
from rest_framework.routers import DefaultRouter
from items.views import ItemViewset
from items.models import Item

router = DefaultRouter()
router.register("items",ItemViewset, basename=Item)
urlpatterns = [
    path("", include(router.urls))
]