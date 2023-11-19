from django.urls import path
from . import views

urlpatterns = [
    path('', views.proind, name = 'proind')
]
