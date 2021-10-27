from django.db import models

# Create your models here.
class City(models.Model):
    name= models.CharField(max_length=100)
    url_img= models.URLField(max_length=255)

    def __str__(self):
        return self.name

class Services(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    id_city= models.ForeignKey(City, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    stars= models.PositiveIntegerField()
    description= models.TextField()
    url_img= models.URLField(max_length=255)

    def __str__(self):
        return self.name

class Comments(models.Model):
    id_hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user_name= models.CharField(max_length=100)
    content= models.TextField(max_length=400)

    def __str__(self):
        template = f'{self.user_name} - comentario - {self.id_hotel.name}'
        return template

class Photos_outside(models.Model):
    id_hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE)
    url_img= models.URLField(max_length=255)
    name_img= models.CharField(max_length=50)

    def __str__(self):
        template = f'fotos facha de {self.id_hotel.name}'
        return template

class Photos_inside(models.Model):
    id_hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE)
    url_img= models.URLField(max_length=255)
    name_img= models.CharField(max_length=50)

    def __str__(self):
        template = f'fotos habitaciones de {self.id_hotel.name}'
        return template

class Services_hotel(models.Model):
    id_hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE)
    id_service= models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        template = f'servicio de {self.id_service.name} del hotel {self.id_hotel.name}'
        return template