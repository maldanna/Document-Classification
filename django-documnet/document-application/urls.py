from django.shortcuts import render
from django.urls import path
from . import views
app_name='okcoolapp1'
urlpatterns=[
    path('home/',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('upload/',views.upload,name='upload'),
    path('result/',views.result,name='result'),
    path('about/', views.about, name='about'),

]