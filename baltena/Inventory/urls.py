from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home, login_user, logout_user, register_user,
    itemview, orderview, customerview, sizeview, suppliersview, priceview, categoryview,
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
    path('orders/',orderview, name='orders'),
    path('customers/',customerview, name='customers'),
    path('size/',sizeview, name='size'),
    path('suppliers/',suppliersview, name='suppliers'),
    path('price/',priceview, name='price-history'),
    path('category/',categoryview, name='category'),
]