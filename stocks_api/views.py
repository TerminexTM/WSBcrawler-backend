from django.shortcuts import render
from rest_framework import generics
from .serializers import StockSerializer
from .models import Stock
# Create your views here.

class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockSerializer
