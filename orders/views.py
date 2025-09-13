from django.db.models import QuerySet
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsManagerOrOwner, IsAuthenticatedAndManagerOrReadOnly


class OrderListCreateView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,IsAuthenticatedAndManagerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at', 'total_price']

    @swagger_auto_schema(operation_summary="List orders", security=[{'Bearer': []}])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    def get_queryset(self) -> QuerySet[Order]:


        user = self.request.user

        print("User:", user)
        print("Authenticated:", user.is_authenticated)
        print("Role:", getattr(user, 'role', 'N/A'))
        print("Headers:", self.request.headers)

        if not user.is_authenticated:
            raise NotAuthenticated("Authentication credentials were not provided.")
        if getattr(user, 'role', None) == 'manager':
            return Order.objects.all()
        return Order.objects.filter(customer=user)

        # print("User:", self.request.user)
        # print("Authenticated:", self.request.user.is_authenticated)
        # print("Role:", getattr(self.request.user, 'role', 'N/A'))

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class OrderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsManagerOrOwner]

    def get_queryset(self) -> QuerySet[Order]:
        user = self.request.user
        if not user.is_authenticated:
            raise NotAuthenticated("Authentication credentials were not provided.")
        if getattr(user, 'role', None) == 'manager':
            return Order.objects.all()
        return Order.objects.filter(customer=user)

