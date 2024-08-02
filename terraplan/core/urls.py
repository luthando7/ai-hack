from django.urls import path
from .views import home, crop_data

urlpatterns = [
    path('', home, name='home'),
    path('crop_data/', crop_data, name='crop-data'),
]