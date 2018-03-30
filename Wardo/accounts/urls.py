#el login y logout atraves de django auth
from django.contrib.auth.views import login, logout
from django.urls import path
from accounts.views import signup

app_name = "accounts"

urlpatterns = [
	path('login',login, {'template_name': 'accounts/login.html'}, name='login'),
	# logout no tiene template, solo nos saca de la sesion y redirecciona
	path('logout',logout, {'next_page':'/'}, name="logout"),
	path('signup',signup, name="signup"),
]
#creo usuarios por defecto con:
# ./manage.py createsuperuser
# 