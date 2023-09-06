from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')
def properties(request):
    return render(request, 'main/properties.html')

def propertyds(request):
    return render(request, 'main/propertyds.html')

