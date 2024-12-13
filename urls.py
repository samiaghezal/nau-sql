from django.urls import path
from ninja import NinjaAPI
from .api import router


api = NinjaAPI()
api.add_router('', router)


urlpatterns = [
    path('api/', api.urls),
]