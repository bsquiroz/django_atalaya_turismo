from rest_framework import serializers
from .models import City, Hotel, Comments, Photos_outside, Photos_inside, Services_hotel

class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = ('__all__')

class CityIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('__all__')

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ('__all__')

class PhotosOutsideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photos_outside
        fields = ('__all__')

class PhotosInsideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photos_inside
        fields = ('__all__')

class ServicesHotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services_hotel
        fields = ('__all__')

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ('__all__')