from django.urls import path, include

from . import api

urlpatterns = [
    path("", api.Fibbo.as_view(), name="fibbonaci-number"),
]