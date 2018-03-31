from comments.views import create_comment
from django.urls import path

app_name = "comments"

urlpatterns = [
	path('createcomment', create_comment, name="createcomment")
]