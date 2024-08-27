from django.urls import path
from . import views

urlpatterns = [
    path('str1/', views.str1, name='str1'),
    path('str2/', views.str2, name='str2'),
    path('str3/', views.str3, name='str3'),
    path('str4/', views.str4, name='str4'),
    path('', views.str1, name='str1')
]