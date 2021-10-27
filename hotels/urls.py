from os import name
from django.urls import path 
from hotels import views

urlpatterns = [
    path('ciudades/', views.cityList, name='cities'),
    path('ciudades/<str:name_city>', views.hotels, name='hotels'),
    path('ciudades/<str:name_city>/<int:pk>', views.hotel, name='hotel')
]