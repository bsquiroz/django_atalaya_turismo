from django.contrib import admin
from .models import City,Services,Hotel,Comments,Photos_outside,Photos_inside,Services_hotel

# Register your models here.
admin.site.register([City,Services,Hotel,Comments,Photos_outside,Photos_inside,Services_hotel])