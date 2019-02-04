from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('criar/', views.post_create, name='post_create'),
    path('editar/<int:id>/', views.post_update, name='post_update'),
    path('deletar/<int:id>/', views.post_delete, name='post_delete'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
]
