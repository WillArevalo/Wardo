from django.urls import path
from products.views import HomeView

urlpatterns = [
	path("", HomeView.as_view(),name="home"),
]