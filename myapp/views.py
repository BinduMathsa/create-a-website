from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.
def myfunctioncall(request):
     return HttpResponse("Hello world")

def myfunctionabout(request):
     return HttpResponse("About Response")

def myfirstpage(request):
   return render(request,'index.html')      

def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary) 

def sign(request):
   return render(request,'1.html')  

def register(request):
   return render(request,'register.html') 

def abou(request):
   return render(request,'about.html') 

def instruct(request):
   return render(request,'instruct.html') 

def view(request):
   return render(request,'view.html') 

def python(request):
   return render(request,'python.html')    

def django(request):
   return render(request,'django.html')    

def java(request):
   return render(request,'java.html')    

def net(request):
   return render(request,'net.html')             

def ps(request):
   return render(request,'ps.php')

def contact(request):
   return render(request,'contact.html')                


