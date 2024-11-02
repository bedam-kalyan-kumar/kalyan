from django.http import HttpResponse
from django.shortcuts import render

def facebook(request):
    return render(request, 'facebook.html')

def home_page(request):
    return render(request, 'home.html')
def instagram(request):
    return render(request, 'instagram.html')
def twitter(request):
    return render(request, 'twitter.html')
def many(request):
    return render(request, 'many.html')
def whatsapp(request):
    return render(request, 'whatsapp.html')