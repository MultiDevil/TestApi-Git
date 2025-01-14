from django.urls import path
from .views import BlogPostList, UserProfileDetail

urlpatterns = [
    path('items/', BlogPostList.as_view(), name='item-list'),
    path('userprofile/<int:user_id>/', UserProfileDetail.as_view(), name='user-profile-detail'),
]
