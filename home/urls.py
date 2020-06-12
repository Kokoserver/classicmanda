
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home" ),
    path('contact', views.contact, name="contact" ),
    path('about', views.about, name="about" ),
    path('terms', views.terms, name="terms" ),
    path('delivery', views.delivery, name="delivery" ),
    path('policy', views.policy, name="policy" ),
    path('vault', views.vault, name="vault" ),
    path('lightning', views.lightning, name="lightning" ),
    path('bateriesandpanels', views.bateriesandpanels, name="bateriesandpanels" ),
    path('mattress', views.mattress, name="mattress" ),
    path('bequipment', views.bequipment, name="bequipment" ),
    path('dishwasher', views.dishwasher, name="dishwasher" ),
    path('search', views.search, name="search" ),
    path('<int:id>/product', views.product, name="product" ),
    path('<int:id>/cart', views.cart, name="cart" )
]