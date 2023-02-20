from django.urls import path, re_path, include
from main import views

urlpatterns = [
    path("", views.index),
    path("results/", views.results),
    path("voting/postuser/", views.postuser),
    path("voting/", views.voting),
]
