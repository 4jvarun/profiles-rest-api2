# from django.urls import path
# from profiles_api import views
#
# url_pattern = [
#
#     path('hello_view/', views.HelloApiView.as_view()),
# ]

from django.urls import path
from django.contrib import admin
from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
