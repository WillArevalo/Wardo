from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=255)
	description = models.TextField(max_length=255)
	price = models.IntegerField()
	slug = models.SlugField()
	categories = models.ManyToManyField('products.ProduCategory')

	#funcion para obtener una url absoluta del producto
	def get_absolute_url(self):
		#return reverse("nombre de nuestra vista", params)
		#queda asi products/<slug:slug>
		return reverse("detail", kwargs={'slug': self.slug})

	def __str__(self):
		return self.title

class ProductImage(models.Model):
	#si un producto se borra sus iamgenes tambien
	#related name para definir la relacion inversa
	#para referir el product con las imagenes
	product = models.ForeignKey(
		'products.Product',
		on_delete=models.CASCADE,
		related_name='images'
	)
	#ImageField referencia una ubicacion
	#Instalo Pillow sobre el proyecto para el manejo de imagenes
	image = models.ImageField()

	def __str__(self):
		return self.image.url	

class ProduCategory(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=255)
	slug = models.SlugField()

	def __str__(self):
		return self.name
