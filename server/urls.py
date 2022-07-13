from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', access),
    path('update', update)
]
