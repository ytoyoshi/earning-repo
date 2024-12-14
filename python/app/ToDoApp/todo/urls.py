from django.contrib import admin
from django.urls import path
from . import views
from .views import TodoList, CreateList, DetailList

urlpatterns = [
    path("list/", TodoList.as_view(),name="list"),
    path("create/", CreateList.as_view(),name="create"),
    path("detail/<int:pk>", DetailList.as_view(),name="detail"),
    path("complete/<int:id>", views.Complete,name="complete"),
]