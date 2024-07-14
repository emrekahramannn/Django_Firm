from django.urls import path
from .views import home, page

urlpatterns = [
    path("", home, name="home",),
    path("<slug:slug>/", page, ),
]
