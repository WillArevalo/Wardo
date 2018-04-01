from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from products.models import Product, LogBuy
from comments.forms import CommentForm
import stripe
from django.conf import settings
# Create your views here.
#vista de home en products
class HomeView(TemplateView):
	template_name='products/home.html'

	#le pasamos en el contexto todos los productos
	def get_context_data(self, *args, **kwargs):
		products = Product.objects.all()
		return {'products': products}

#vista para detalle del prodcuto
#solo si pongo el nombre del template con un guin bajo y detail
# el toma el archivo por defecto
class ProductDetailView(DetailView):
	model = Product

	def get_context_data(self, *args, **kwargs):
		#para que no se sobrescriba si no escribir al final del context
		context = super().get_context_data(*args, **kwargs)
		comment_form = CommentForm()
		context['comment_form'] = comment_form
		return context

class ProductBuyView(DetailView):
	model = Product
	template_name = 'products/buy.html'

	#Recolectando el token que da Stripe en el post
	def post(self, request,*args, **kwargs):
		stripe.api_key = settings.STRIPE_API_KEY
		#En el post vienen el token en este param
		token = request.POST['stripeToken']
		#Ya que estamos utilizando un detailView podemos traer el producto asi
		product = self.get_object()
		error_message = None
		try:
			#charge Genera un carga unico
			charge = stripe.Charge.create(
		            amount=product.price,
		            currency='usd',
		            description="cobro por {}".format(product.title),
		            statement_descriptor="cobro Wardo",
		            source=token
				)
		except stripe.error.CardError as e:
			body = e.json_body
			err = body['error']
			error_message = err['message']
		except stripe.error.StripeError as e:
			error_message = "Can't process your payment, please try again later"

		if error_message:
			return render(request, "products/failed.html", {'error_message': error_message, 'product': product})
		
		buyer = None
		if request.user.is_authenticated:	
			buyer = request.user

		#guardo el registro si fue exitoso
		LogBuy.objects.create(
			product = product,
			user = buyer,
		)
		
		#Opcional enviar el debug de stripe
		return render(request, "products/success.html", {'debug_info': charge, 'product': product})