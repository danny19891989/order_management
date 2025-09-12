from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Order
from .serializers import OrderSerializer

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
