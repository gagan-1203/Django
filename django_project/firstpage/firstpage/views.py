from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data ={
        'title':'Home new',
        'bdata':'Welcome to the first page',
        'clist': ['PHP','Java','Django'],
        'numbers': [10,20,30,40,50],
        'student_details':[
            {'name':'Shivam','phone':15189527852},
            {'name':'Jhon','phone':785265268412}
        ]
    }
    return render(request,"index.html",data)

#def aboutUS(request):
    return HttpResponse("Hello World")

#def Login(request,loginpage):
    return HttpResponse(request,loginpage)