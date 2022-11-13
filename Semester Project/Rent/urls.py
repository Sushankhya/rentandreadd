from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='homepage'),
    path('books/',views.books,name='book'),
    path('books/<str:pk>/',views.catoBooks, name = 'cato-books'),
    path('faq/',views.faq,name='faq'),
    path('users/', include('users.urls')),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkOut, name='check-out'),
    path('upadate-cart/', views.updateCart, name = 'update-cart'),
    path('search/',views.search,name='search'),
    path('bookview/<str:pk>',views.bookview,name='bookview'),
  
    

]
