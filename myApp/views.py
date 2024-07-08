from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register



# Create your views here.
def Name (request):
    return render(request,'Name.html')
def About (request):
    return render(request,'About.html')
def Contacts (request):

    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        mssg = request.POST['mssg']

        register = Register(fname=fname, email=email, mssg=mssg)
        register.save()
        print("happy birthday")

    return render(request, 'Contacts.html')
def Home (request):
    return render(request, 'Home.html')
def Portfolio (request):
    return render(request, 'Portfolio.html')


