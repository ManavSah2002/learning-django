from django.shortcuts import render,HttpResponse

def index (request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")