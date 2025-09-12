from django.urls import path, include

urlpatterns = [
    path('v1/auth/', include('userauth.urls')),
    path('v1/orders/', include('orders.urls')),
]
