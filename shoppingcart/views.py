
from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        # Override the create method to associate the cart item with a specific cart
        cart_id = self.request.data.get('cart')  # Assuming you send 'cart' in your POST data
        cart = Cart.objects.get(pk=cart_id)
        serializer.save(cart=cart)

class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
