from curses.ascii import NUL
from email.policy import default
from enum import auto
from operator import mod
from statistics import mode
import sys
import os
from tkinter.tix import Tree
sys.path.append("..")
from users.models import Profile
from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 150, default = 'none')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class BookReview(models.Model):
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey('Books', on_delete = models.CASCADE)
    comment = models.TextField(null = True, blank = True)
    stars = models.IntegerField(default = 0, null=True, blank=True, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    reviewed_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.book)

    

class Books(models.Model):
    title = models.CharField(max_length = 200, default = '')
    author = models.CharField(max_length = 200, default = 'Unknown')
    description = models.TextField(null = True, blank = True)
    price = models.IntegerField(default = 0)
    book_cover = models.ImageField(null =True, blank = True, upload_to = 'book-covers/', default = 'book-covers/default-book-cover.jpg')
    category = models.ManyToManyField(Category, blank = True)
    available = models.BooleanField(default= True)
    added_on = models.DateTimeField(auto_now_add=True)
    in_cart = models.BooleanField(default = False, editable = False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

class FAQ(models.Model):
    question = models.CharField(max_length = 500, default = '')
    answer = models.TextField(null = True, blank = True)
    added_on = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.question)

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete = models.SET_NULL, blank = True, null = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)
    transection_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.customer)

    @property
    def getCartTotal(self):
        orderedItems = self.orderitem_set.all()
        total = sum([item.product.price for item in orderedItems])
        return total
    def getTotalItems(self):
        total = 0
        orderedItems = self.orderitem_set.all()
        for item in orderedItems:
            total = total + 1
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Books, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE, null = True)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return str(self.product.title)
    



class ShippingDetails(models.Model):
    customer = models.ForeignKey(Profile, on_delete = models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null = True)
    state = models.CharField(max_length = 200, null = False)
    city = models.CharField(max_length = 200, null = False)
    address = models.CharField(max_length = 200, null = False)
    date_added = models.DateTimeField(auto_now_add = True)
    phone_numer = models.CharField(max_length = 20, default = 'N/A')
    def __str__(self):
        return str(self.address)