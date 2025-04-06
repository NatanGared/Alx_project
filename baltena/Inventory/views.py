from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Category, Item, Size, Supplier, Customer, PriceHistory, IncomingItem, Order
from .serializers import (
    CategorySerializer, ItemSerializer, SizeSerializer, SupplierSerializer,
    CustomerSerializer, PriceHistorySerializer, IncomingItemSerializer, OrderSerializer,
)
from .forms import SignUpForm
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission

def home(request):
    items = Category.objects.all()
    return render(request, 'home.html',{'items': items})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error while logging in, Please try again!")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            viewer_group, created = Group.objects.get_or_create(name='viewer')
            user.groups.add(viewer_group)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfuly registered!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please try again.")
            print(form.errors)
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and in the 'admin' group
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='admin').exists()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class IncomingItemViewSet(viewsets.ModelViewSet):
    queryset = IncomingItem.objects.all()
    serializer_class = IncomingItemSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

def itemview(request):
    items = Item.objects.all()
    return render(request, 'item.html',{'items': items})

def orderview(request):
    items = Order.objects.all()
    return render(request, 'order.html',{'items': items})

def customerview(request):
    items = Customer.objects.all()
    return render(request, 'customer.html',{'items': items})

def sizeview(request):
    items = Size.objects.all()
    return render(request, 'size.html',{'items': items})

def suppliersview(request):
    items = Supplier.objects.all()
    return render(request, 'supplier.html',{'items': items})

def priceview(request):
    items = PriceHistory.objects.all()
    return render(request, 'price.html',{'items': items})

def categoryview(request):
    items = Category.objects.all()
    return render(request, 'category.html',{'items': items})