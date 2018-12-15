from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
	return HttpResponse('Olá Mundo!');

def about(request):
	return HttpResponse('Sobre nós.')

def contact(request):
	return HttpResponse('Página de contato.')