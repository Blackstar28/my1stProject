from django.shortcuts import render

# Create your views here.
def Name (request):
    return render(request,'Name.html')
def About (request):
    return render(request,'About.html')
def Contacts (request):
    return render(request, 'Contacts.html')
def Home (request):
    return render(request, 'Home.html')
def Portfolio (request):
    return render(request, 'Portfolio.html')
