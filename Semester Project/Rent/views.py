from asyncio.windows_events import NULL
from itertools import count
import json
from multiprocessing import context
from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import random
import copy
sys.path.append("..")

# Create your views here.
def index(request):
    return render(request,'Rent/homepage.html')
def books(request):
    books = Books.objects.all()
    books = list(books)
    random.shuffle(books)
    topRated = []
    noOfTop = 0
    nepaliBooks = []
    noOfNep = 0
    categories = Category.objects.all()
    if request.user.is_authenticated:
        customer = request.user.profile        
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        for book in books:
            for item in items:
                if item.product == book:
                    book.in_cart = True
    else:
        items = []
        

    index = []
    for book in books:
        flag = False
        for cat in book.category.all():
            if cat.name == 'Top Rated' and noOfTop<4:
                topRated.append(copy.deepcopy(book))
                noOfTop = noOfTop + 1
                flag = True
                break
            if cat.name == "Nepali" and noOfNep<4:
                nepaliBooks.append(copy.deepcopy(book))
                noOfNep = noOfNep + 1
                flag = True
                break
        if flag:
            index.append(books.index(book))

    for i in index:
        books[i] = None
    # books_page = True
    context = {'books': books, 'categories': categories, 'top_rated': topRated, 'nepaliBook': nepaliBooks,'cart':items,'books_page':True}
    return render(request,'Rent/books.html', context)

def catoBooks(request, pk):
    cateId = Category.objects.get(name = pk)
    books = Books.objects.filter(category=cateId)
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        for book in books:
            for item in items:
                if item.product == book:
                    book.in_cart = True
    categories = Category.objects.all()
    context = {'books':books, 'category_name':pk, 'categories': categories, 'books_page': True}
    return render(request, 'Rent/catobooks.html', context)


def faq(request):
    faqs = FAQ.objects.all()
    context = {'faqs': faqs}
    return render(request,'Rent/faq.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        context = {'items': items, 'order': order}       
        return render(request, 'Rent/cart.html', context)
    else:
        return render(request, 'login')

def checkOut(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        context = {'items': items, 'order': order}       
        return render(request, 'Rent/checkout.html', context)
    else:
        return render(request, 'login')
    

def updateCart(request):
    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']
    customer = request.user.profile
    book = Books.objects.get(id = bookId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = book)
    print("action ----------------------", action)
    if action == 'remove':
        orderItem.delete()
    order.save()
    return JsonResponse('Item was added', safe=False)


def search(request):
    query=request.GET['query']
    books= Books.objects.filter(title__icontains=query)

    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        for book in books:
            for item in items:
                if item.product == book:
                    book.in_cart = True
    else:
        item = []
    categories = Category.objects.all()

    params={'books':books,'query':query, 'categories': categories, 'books_page': True}
    return render(request,'Rent/search.html',params)


def  bookview(request,pk):
    book=Books.objects.get(id=pk)
    if (request.method == 'POST'):
        user_feedback = request.POST.get('comment')
        currentUser = request.user.profile
        review = BookReview(comment = user_feedback, reviewer = currentUser,book = book)
        review.save()
        
    cat = Category.objects.filter(books__title = book)
    relatedBooks = Books.objects.filter(category=cat[0])
    print(relatedBooks)
    relatedBooks = list(relatedBooks)
    random.shuffle(relatedBooks)
    relatedBooks = relatedBooks[0:7]
    context={"book":book, 'related':relatedBooks}
    return render(request,'Rent/bookview.html',context)