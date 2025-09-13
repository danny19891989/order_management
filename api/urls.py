from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('v1/auth/', include('userauth.urls')),
    path('v1/orders/', include('orders.urls')),
]

# swagger configurations only for development environment
schema_view = get_schema_view(
    openapi.Info(
        title="Order Management API",
        default_version='v1',
        description="API documentation for your Django order management system",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
        path('v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

