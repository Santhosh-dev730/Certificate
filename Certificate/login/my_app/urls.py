from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.create,name="create"),
    path('read/',views.read,name="read"),
    path('update/<str:id>/',views.update,name="update"),
    path('delete/<str:id>/',views.delete,name="delete")
]