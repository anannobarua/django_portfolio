from django.urls import path
from . import views

urlpatterns = [
    path('anannosapp/', views.index, name='index.html'),
]
