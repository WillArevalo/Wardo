from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from products.models import Product
from comments.forms import CommentForm
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

	def get_context_data(self, *args, **kwargs):
		#para que no se sobrescriba si no escribir al final del context
		context = super().get_context_data(*args, **kwargs)
		comment_form = CommentForm()
		context['comment_form'] = comment_form
		return context