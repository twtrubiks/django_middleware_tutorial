from django.urls import path
from . import views

urlpatterns = [
    # /musics/
    path("", views.index, name="index"),
]
