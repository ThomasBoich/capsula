from django.contrib import admin
from django.urls import path, include
from .views import get_category, news

urlpatterns = [
    path('', news, name="news"),
    path('category/<int:category_id>/', get_category, name="category"),
]
