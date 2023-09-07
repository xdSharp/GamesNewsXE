from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def reviews(request):
    return render(request, 'main/reviews.html')

def guides(request):
    return render(request, 'main/guides.html')