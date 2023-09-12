# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin_data/', views.admin_data_list, name='admin_data_list'),
]
