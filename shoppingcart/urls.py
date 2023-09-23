from django.urls import path
from . import views

urlpatterns = [
    path('carts/', views.CartList.as_view(), name='cart-list'),
    path('carts/<int:pk>/', views.CartDetail.as_view(), name='cart-detail'),
    path('cartitems/', views.CartItemList.as_view(), name='cart-item-list'),
    path('cartitems/<int:pk>/', views.CartItemDetail.as_view(), name='cart-item-detail'),
    
    
    path('access_token/', views.generateAccessToken, name='generateAccessToken'),
    path('stk_push/', views.initiate_stk_push, name='initiate_stk_push'),
]
