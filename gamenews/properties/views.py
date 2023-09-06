from django.shortcuts import render

def properties(request):
    return render(request, 'properties.html')