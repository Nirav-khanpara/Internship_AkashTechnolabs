from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request, 'myform.html')


def process(request):
    # a = int(request.POST['num1'])
    # b = int(request.POST['num2'])

    data = {

    'method' : request.method,
    'FirstName' : request.POST['fname'],
    'MiddleName' : request.POST['mname'],
    'LastName' : request.POST['lname'],
    'Email' : request.POST['email'],
    'BirthDate' : request.POST['birthdate'],
    'MobileNo'  : request.POST['mobileno'],
    'LocalAddress' : request.POST['localaddress'],
    'PermanentAddres' : request.POST['permanentaddress'],
    'Pincode' : request.POST['pincode'],
    'Password' : request.POST['password'],
    'ConfirmPassword' : request.POST['confirmpass'],

    }

    return render(request, 'answer.html', {'info':data})



