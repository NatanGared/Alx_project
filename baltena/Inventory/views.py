from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Category, Item, Size, Supplier, Customer, PriceHistory, IncomingItem, Order
from .serializers import (
    CategorySerializer,
    ItemSerializer,
    SizeSerializer,
    SupplierSerializer,
    CustomerSerializer,
    PriceHistorySerializer,
    IncomingItemSerializer,
    OrderSerializer,
)

def home(request):
    items = Category.objects.all()
    return render(request, 'home.html',{'items': items})

def login_user(request):

    return render(request, 'login.html',{})

def logout_user(request):
    return redirect(request, 'login.html',{})
#class HomeView(TemplateView):
    template_name = "home.html"

#class LogInView(TemplateView):
    template_name = "login.html"


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer

class IncomingItemViewSet(viewsets.ModelViewSet):
    queryset = IncomingItem.objects.all()
    serializer_class = IncomingItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer