from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
]
