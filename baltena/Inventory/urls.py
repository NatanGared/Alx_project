from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home, login_user, logout_user, register_user,
    CategoryViewSet,
    ItemViewSet,
    SizeViewSet,
    SupplierViewSet,
    CustomerViewSet,
    PriceHistoryViewSet,
    IncomingItemViewSet,
    OrderViewSet,
)
#from .views import HomeView, LogInView


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'price-history', PriceHistoryViewSet)
router.register(r'incoming-items', IncomingItemViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('',home, name='home'),
    path('api/', include(router.urls)),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('register/',register_user, name='register'),
    path('items/',itemview, name='items'),
    path('orders/',logout_user, name='orders'),
    path('customers/',logout_user, name='customers'),
    path('size/',logout_user, name='size'),
    path('suppliers/',logout_user, name='suppliers'),
    path('price/',logout_user, name='price-history'),
]