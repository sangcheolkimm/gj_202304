from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def main(request) :    
#     return render(request,
#                   'frontapp/main.html',
#                   {})
#     # return HttpResponse("go go...")

def index(request) :    
    return render(request,
                  'frontapp/index.html',
                  {})
    # return HttpResponse("go go...")

def imageView(request) :
    return render(request,
                  'frontapp/01_image.html',
                  {})

def cssView1(request) :
    return render(request,
                  'frontapp/02_css1.html',
                  {})

def cssView2(request) :
    return render(request,
                  'frontapp/02_css2.html',
                  {})

def cssView3(request) :
    return render(request,
                  'frontapp/02_css3.html',
                  {})

def cssView4(request) :
    return render(request,
                  'frontapp/01_javascript1.html',
                  {})

def cssView5(request) :
    return render(request,
                  'frontapp/01_javascript2.html',
                  {})

def cssView6(request) :
    return render(request,
                  'frontapp/01_javascript3.html',
                  {})