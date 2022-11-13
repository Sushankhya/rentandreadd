from django.contrib import admin
from .models import Category, BookReview, Books, FAQ, Order, OrderItem, ShippingDetails
# Register your models here.

admin.site.register(Category)
admin.site.register(Books)
admin.site.register(BookReview)
admin.site.register(FAQ)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingDetails)