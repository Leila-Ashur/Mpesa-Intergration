# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import authenticate, login
# from .models import CustomUser
# from .serializers import UserSerializer

# class UserRegistration(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLogin(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username')
#         phone_number = request.data.get('phone_number')
#         password = request.data.get('password')

#         user = authenticate(request, username=username, phone_number=phone_number, password=password)

#         if user is not None:
#             login(request, user)
#             return Response({'message': 'Login successful'})
#         return Response({'message': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)



views.py

from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from User_Registrations.models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Category
from .serializers import CategorySerializer
from .models import VirtualItem
from .serializers import VirtualItemSerializer
from rest_framework import generics


from . import roles
from . import models


User = get_user_model()

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            gamer_role, created = roles.objects.get_or_create(name="Gamer")
            user.roles.add(gamer_role)

            # Include a success message in the response
            response_data = {
                "message": "Registration successful. You have been logged in."
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRegistrationUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id' 

class UserRegistrationDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class UserLoginView(APIView):
    def post(self, request):
        username =request.data.get('username')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({'Invalid Credentials'},status= status.HTTP_401_UNAUTHORIZED)
        if user.check_password (password):
            login (request,user)
            return Response({'Login succesfull'},status=status.HTTP_200_OK)
        else:
            return Response({'Invalid Credentials'},status= status.HTTP_401_UNAUTHORIZED)
