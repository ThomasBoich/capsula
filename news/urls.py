from django.contrib import admin
from django.urls import path,include
from .views import get_category, news
from .models import *


urlpatterns = [
    path('', news),
    path('category/<int:list_category>/', get_category),
]