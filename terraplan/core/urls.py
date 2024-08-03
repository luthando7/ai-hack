from django.urls import path
from .views import home, crop_data

urlpatterns = [
    path('', home, name='home'),
    path('crop_prediction/', crop_data, name='crop-data'),
]