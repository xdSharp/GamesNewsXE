from django.shortcuts import render

def guides(request):
    return render(request, 'guides.html')
