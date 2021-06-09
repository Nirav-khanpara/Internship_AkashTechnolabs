from django.shortcuts import render
from .forms import StudentRegi
from .models import User

# Create your views here.

def sturegi(request):
    if request.method=='POST':
        data = StudentRegi(request.POST)
        if data.is_valid():
            
            nm = data.cleaned_data['name']
            em = data.cleaned_data['email']
            pw = data.cleaned_data['password']

            obj = User(name=nm, email=em, password=pw)
            obj.save()
    else:
        data = StudentRegi()
        print('This is GET')
    
    return render(request, 'enroll/sturegi.html', {'form':data})