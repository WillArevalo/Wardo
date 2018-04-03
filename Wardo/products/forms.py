from django import forms
from products.models import Product
#form en vista de detalle y en vista de crear un comentario
class SearchForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = [
			'title',
		]