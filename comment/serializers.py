from rest_framework import serializers
from comment.models import ReviewComments

class CommentSerializer(serializers.ModelSerializer):
      
      class Meta:
         model=ReviewComments
         fields= "__all__"