from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_index, name='index'),
	path('home',views.show_home, name='home'),
    path('login',views.show_login, name='login'),

    # Livro
    path('livro_list',views.livro_list, name='livro_list'),
    path('livro_create',views.livro_create, name='livro_create'),
    path('livro_update/<int:codigo_livro>',views.livro_update, name='livro_update'),
    path('livro_delete/<int:codigo_livro>',views.livro_delete, name='livro_delete'),

]
