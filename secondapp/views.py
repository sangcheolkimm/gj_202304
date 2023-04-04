from django.shortcuts import render

## 사용자 브라우저로 응답을 하기 위한
# 라이브러리 불러들이기
from django.http import HttpResponse

# Create your views here.
def testPage(request) :
    return HttpResponse("Django OK...")


#최초 페이지
def index(request) :
    msg='''
       <h3>Index Page 입니다.</h3>
       <hr/>
       <p>
           HTML 코드 잘 실행됩니다.
       </P>
    '''
    # return HttpResponse(msg)
    return render(request,
                  'secondapp/index.html',
                  {'key':'value잘 나옴',
                   'key2' : 'value2...'})

def indexx(request) :
    msg='''
       <h3>Index Page 입니다.</h3>
       <hr/>
       <p>
           HTML 코드 잘 실행안됩니다.
       </P>
    '''
    # return HttpResponse(msg)
    return render(request,
                  'secondapp/indexx.html',
                  {'key':'value잘 나옴',
                   'key2' : 'value2...'})

def cssTestView(request) :
    msg='''
       <h3>css Page 입니다.</h3>
       <hr/>
       <p>
        .
       </P>
    '''
    # return HttpResponse(msg)
    return render(request,
                  'secondapp/css_test.html',
                  {})