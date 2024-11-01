from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('',views.lista_produtos, name='lista_produtos'),
        path('criar_produto/',views.produtos_create, name='criar_produto'),
        path('delete/<int:produto_id>/', views.delete_produto, name='delete_produto')
]



