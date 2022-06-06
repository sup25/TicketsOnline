from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('cart/', views.carts, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]