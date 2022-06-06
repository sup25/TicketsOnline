from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.stores, name="stores"),
	path('cart/', views.carts, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]