from django.urls import path
from .views import *

urlpatterns = [
    path("", products_list, ),
    path("<int:id>/", product_detail)
]
