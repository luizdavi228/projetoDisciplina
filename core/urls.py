from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_home, name='home'),
    path('login',views.show_login, name='login'),
]
