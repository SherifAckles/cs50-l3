from django.shortcuts import render
from django.http import HttpResponse



# def greet(request,name):
#     #make httprequest to render just a str
#     return HttpResponse(f"Hello,{name.capitalize()}")

# def index(request):
#     # to render the whole html file
#  return render(request,"hello/index.html")

# def sherif(request):
    
#     return HttpResponse("Hello, Sherif :)")

# def david(request):
#     return HttpResponse("Hello, David :)")

def greet(request,name):
    return render(request,"hello/greet.html",{
        "name":name.capitalize()
        
    })
    