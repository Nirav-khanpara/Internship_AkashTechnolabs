from django.shortcuts import render
from .forms import StudentRegi

# Create your views here.
def sturegi(request):
    if request.method=='POST':
        data = StudentRegi(request.POST)
        if data.is_valid():
            print('Form is validated.')
            print('Name:',data.cleaned_data['name'])
            print('Email:', data.cleaned_data['email'])
            print('Password:', data.cleaned_data['password'])
            print('Terms and Conditions:',data.cleaned_data['agree'])
        else:
            print('Form is invalid.')
    else:
        data = StudentRegi()
        print('This is GET method')
    
    return render(request, 'enroll/sturegi.html', {'form':data})