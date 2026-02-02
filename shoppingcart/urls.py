from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='shoppingcart.index'),
    path('<int:id>/add/', views.add, name='shoppingcart.add'),
    path('clear/', views.clear, name='shoppingcart.clear'),
    path('purchase/', views.purchase, name='shoppingcart.purchase'),
]