from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CitySerializer, CityIdSerializer, HotelSerializer,  CommentsSerializer, PhotosOutsideSerializer, PhotosInsideSerializer, ServicesHotelSerializer

from .models import City, Hotel, Comments, Photos_outside, Photos_inside, Services_hotel

# Create your views here.
@api_view(['GET'])
def cityList(request):
    cities = City.objects.all()
    print(cities)
    serializer = CitySerializer(cities, many=True)

    return Response({
        'cities': serializer.data
    })

@api_view(['GET'])
#!name_city es lo que viene por parametros en la url
def hotels(request, name_city):
    #!En la variable city me queda el query despues de filtrar por el nombre 
    #!debo de pasarlo por el serializer el cual me devuelve un array 
    #!como es uno le pongo cero y extraigo el id

    city = City.objects.filter(name__iexact=name_city)
    city_name = CityIdSerializer(city, many=True)
    cityId = city_name.data[0]['id']

    #!teniendo el id, voy a irme a la tabla de hoteles y voy a filtrar por 
    #!el campo id con cityId despues de esto serializo los datos

    hotels = Hotel.objects.filter(id_city=cityId)
    serializer = HotelSerializer(hotels, many=True)

    return Response({
            'hotels' : serializer.data
        }
    )

@api_view(['GET'])
def hotel(request, name_city, pk):
    hotel = Hotel.objects.filter(id=pk)
    comments = Comments.objects.filter(id_hotel=pk)
    photos_outside = Photos_outside.objects.filter(id_hotel=pk)
    photos_inside = Photos_inside.objects.filter(id_hotel=pk)
    services = Services_hotel.objects.filter(id_hotel=pk)

    serializer_hotel = HotelSerializer(hotel, many=True)
    serializer_comments = CommentsSerializer(comments, many=True)
    serializer_photos_outside = PhotosOutsideSerializer(photos_outside, many=True)
    serializer_photos_inside = PhotosInsideSerializer(photos_inside, many=True)
    serializer_services = ServicesHotelSerializer(services, many=True)

    photos = {
        "photos_outside": serializer_photos_outside.data,
        "photos_inside": serializer_photos_inside.data,
    }

    return Response({
            'hotel' : serializer_hotel.data,
            'comments': serializer_comments.data,
            'photos': photos,
            "services": serializer_services.data,
        }
    )