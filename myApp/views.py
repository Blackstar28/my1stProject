from django.shortcuts import render

# Create your views here.
def helloworld (request):
    return render(request,'HelloWorld.html')
def testPath (request):
    return render(request, 'testPath.html')
def testPath1 (request):
    return render(request, 'testPath1.html')