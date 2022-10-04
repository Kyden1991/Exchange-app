from django.urls import path
from .views import forms

urlpatterns = [
    path('forms/', forms)
]