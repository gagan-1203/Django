from django.shortcuts import render

# Create your views here.
def Homepage(request):
    return render (request, 'homepage.html')

def LoginPage(request):
    return render (request, 'login.html')

def SignupPage(request):
    return render (request, 'signup.html')