"""
API URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('convert/', views.convert_to_ascii, name='convert_to_ascii'),
    path('info/', views.api_info, name='api_info'),
    path('', views.index, name='index'),
]

