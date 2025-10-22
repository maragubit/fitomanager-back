from .models import Category, Post
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class BlogSerializer(serializers.ModelSerializer):
    author=UserSimpleSerializer()
    class Meta:
        model=Post
        fields="__all__"
        depth=1
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']