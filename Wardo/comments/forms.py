from django import forms
from comments.models import Comment
#form en vista de detalle y en vista de crear un comentario
class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = [
			'content',
			'product'
		]