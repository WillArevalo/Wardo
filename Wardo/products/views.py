from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from products.models import Product
# Create your views here.
#vista de home en products
class HomeView(TemplateView):
	template_name='products/home.html'

	#le pasamos en el contexto todos los productos
	def get_context_data(self, *args, **kwargs):
		products = Product.objects.all()
		return {'products': products}

#vista para detalle del prodcuto
#solo si pongo el nombre del templatecon un guin bajo y detail
# el toma el archivo por defecto
class ProductDetailView(DetailView):
	model = Product

