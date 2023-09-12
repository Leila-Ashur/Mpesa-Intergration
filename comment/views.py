from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from comment.models import ReviewComments
from .serializers import CommentSerializer
from .models import ReviewComments
from rest_framework import status


class CommentsListView(APIView):
    def get(self, request):
        comments = ReviewComments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsDetailView(APIView):
    def get(self,request,id,format=None):
        comments = ReviewComments.objects.get(id=id)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)


    def put(self,request,id,format=None):
        comments = ReviewComments.objects.get(id=id)
        serializer = CommentSerializer(comments,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id,format=None):
        comments = ReviewComments.objects.get(id=id)
        comments.delete()
        return Response("comment deleted", status=status.HTTP_204_NO_CONTENT)