from django.urls import path, include
from django.contrib import admin
from profiles_api import views

from rest_framework.routers import DefaultRouter
#
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
# 
# from django.urls import path, include
#
# from rest_framework.routers import DefaultRouter
#
#
# router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# router.register('profile', views.UserProfileViewSet)
# router.register('feed', views.UserProfileFeedViewSet)
#
# urlpatterns = [
#     path('hello-view/', views.HelloApiView.as_view()),
#     path('login/', views.UserLoginApiView.as_view()),
#     path('', include(router.urls)),
# ]
