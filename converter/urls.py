from django.urls import path 
from .views import *
urlpatterns = [
    path('', converter_view, name='converter'),  # URL for the currency converter view
]
