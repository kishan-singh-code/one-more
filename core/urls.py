from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path("", views.index, name='index'),
    path('portfolio',views.portfolio, name="portfolio"),
]