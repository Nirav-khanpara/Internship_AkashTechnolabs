from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'Home.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')