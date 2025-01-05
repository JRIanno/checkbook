from django.urls import path
from . import views

urlpatterns = [
    path('checking/', views.checking, name='checking'),
]