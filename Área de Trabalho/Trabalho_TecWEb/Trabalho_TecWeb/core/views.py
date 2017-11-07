from django.shortcuts import render
from django.http import request
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.

def index(request):
 	return render(request,"index.html")

def noticias(request):
	return render (request,"noticias.html")

def login(request):
	return render (request,"login.html")


def graduacao(request):
	return render (request,"graduacao.html")


def novaDisciplina(request):
	return render (request,"novaDisciplina.html")

def uploadFoto(request):
	return render (request,"upLoadFoto.html")

def mostraFoto(request):
	return render (request,"mostraFoto.html")	