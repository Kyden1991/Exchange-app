from django.urls import path
from .views import charts

urlpatterns = [
    path('charts/', charts, name='charts')
]