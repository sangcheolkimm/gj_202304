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
##[html]##
def htmlview01(request) :
    return render(request,
                  'frontapp/html/01_html.html',
                  {})

def linkview(request) :
    return render(request,
                  'frontapp/html/02_link.html',
                  {})
def linkview2(request) :
    return render(request,
                  'frontapp/html/03_link.html',
                  {})
def cssview(request) :
    return render(request,
                  'frontapp/html/04_css.html',
                  {})

def tableview(request) :
    return render(request,
                  'frontapp/html/05_table.html',
                  {})
def tableview2(request) :
    context={'id':'b001',
                   'name':'홍길동2',
                   'addr':'광주광역시 소촌동 1-2'}
    c_list=[context, context, context]
    return render(request,
                  'frontapp/html/06_table.html',
                  {'c_list':c_list})
def ulview(request) :
    return render(request,
                  'frontapp/html/07_ul.html',
                  {})
def ulview1(request) :
    return render(request,
                  'frontapp/html/08_div.html',
                  {})
def divview2(request) :
    return render(request,
                  'frontapp/html/09_div.html',
                  {})
def iframeview(request) :
    return render(request,
                  'frontapp/html/10_iframe.html',
                  {})
def cssTableview(request) :
    return render(request,
                  'frontapp/css/01_table.html',
                  {})
                                    