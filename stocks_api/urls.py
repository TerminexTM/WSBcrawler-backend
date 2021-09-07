from django.urls import path
from . import views

urlpatterns = [
    path('api/stocks', views.StockList.as_view(), name='stock_list'),
    path('api/stocks/<int:pk>', views.StockDetail.as_view(), name='stock_detail'),
]
