from django.shortcuts import render,HttpResponse

def index (request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")
def about (request):
    return HttpResponse("This is about page")

def services (request):
    return HttpResponse("This is service page")

def contact (request):
    return HttpResponse("This is contact page")

