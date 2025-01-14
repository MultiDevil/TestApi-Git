from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost, UserProfile
from .serializer import BlogPostSerializer, UserProfileSerializer
# Create your views here.
class BlogPostList(APIView):
    def get(self,request):
        blogpost = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogpost, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
            blogpost = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"error":"Item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogPostSerializer(blogpost,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            blogpost = BlogPost.objects.get(pk=pk)
        except blogpost.DoesNotExist:
            return Response({"error":"Item not found"}, status=status.HTTP_404_NOT_FOUND) 
        
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserProfileDetail(APIView):
    def get(self,request, user_id):
        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            return Response({"error":"UserProfile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
    
    def put(self, request, user_id):
        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            return Response({"error":"UserProfile note found"},status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user_profile,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            return Response({"error":"UserProfile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)