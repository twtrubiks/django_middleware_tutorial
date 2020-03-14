from django.urls import path

from . import views

urlpatterns = [
    # ex: /musics/
    path('', views.index, name='index'),
]