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
def cssTableview2(request) :
    return render(request,
                  'frontapp/css/02_table.html',
                  {})
def cssNavview2(request) :
    return render(request,
                  'frontapp/css/03_table.html',
                  {})
def jsInputFormView(request) :
    return render(request,
                  'frontapp/js/01_inputForm.html',
                  {'no':'20',
                   'mem_id':'a001222',
                   'mem_pass':'qwer'})

##입력 폼에서 넘어오는 값 처리
#- 브라우저에서 url입력해서 들어오면 안됨(오류 발생)
#오류 원인: 전달받는 값이 없기 때문..
#-입력 폼의 버튼(이벤트)를 통해서만 접근 가능한 함수
def jsLogin(request) :
    ##처리 순서
    #1.요청 데이터 받기
    #전송 방식에 따라 구분하여 받기: 조건처리
    #- 모든 데이터는 딕셔너리 타입으로 전송됨
    #-POST 및 GET은 딕셔너리 변수가 됨
    if request.method=='POST':
        no = request.POST['no']
        mem_id = request.POST['mem_id']
        mem_pass = request.POST['mem_pass']
    elif request.method=='GET':        
        no = request.GET['no']
        mem_id = request.GET['mem_id']
        mem_pass = request.GET['mem_pass']
    #2. 요청 데이터를 이용 db 처리
    #-Database에 임의 테이블 (testTB)이 있다고 가정
    #-컬럼은 p_id, p_pw가 있다고 가정
    p_id='a001'
    p_pw='asdf'
    
    """
       아래 if (mem_id==p_id) and (mem_pass==p_pw): 조건을
       sql구문으로 만들어 주세요..
       테이블 (testTB), 컬럼은 p_id, p_pw, p_no
    """
    '''
    select * from testTB 
       where mem_id==p_id and mem_pass==p_pw
    -전송받은 값을 모두 저장시키는 sql 구문?
    
    insert into testTB (no, p_id and p_pw)
    valuses(no, mem_id, mem_pass)

    -no와 패스워드의 값을 전송받은 값으로 수정하려고 합니다.
    -단 아이디가 mem_id로 전송받은 아이디에 대하여
    update tesetTB
        Set no= no,
          p_pw=mem_pass
      where p_id = mem_id

      -전송받은 아이디에 대한 정보를 삭제해 주세요..
      delete from testTB
      where p_id=mem_id
       
    '''
    ### 전송받은 mem_id와 p_id가 같고,
    #  mem_pw와 p_pw가 같다면 아래처럼 전달받은 값 모두 응답
    # -아이디 또는 패스워드 중에 하나라도 같지 않다면
    # 응답 메세지(rs_msg)로 '아이디 또는 패스워드가 같지 않습니다.'를 
    # 응답해 주려고 합니다. 
#     if (mem_id==p_id) and (mem_pass==p_pw):
#    #3. db처리 결과를 응답하기(html 파일 또는 메세지 이용)
#       rs_msg='no={}/mem_id={}/mem_pass={}'.format(no,mem_id,mem_pass)
#       return HttpResponse(rs_msg)

#     else :
#         rs_msg='아이디 또는 패스워드가 같지 않습니다.'
   
       
    

#     #3. db처리 결과를 응답하기(html 파일 또는 메세지 이용)
#     rs_msg='no={}/mem_id={}/mem_pass={}'.format(no,mem_id,mem_pass)
#     return HttpResponse(rs_msg)

    if (mem_id==p_id) and (mem_pass==p_pw):
      #3. db처리 결과를 응답하기(html 파일 또는 메세지 이용)
        rs_msg='''
        <script type='text/javascript'>
           alert('정상적으로 로그인 되었습니다!!');
           location.href = '/front/';
        </script>   
      '''

    else :
        rs_msg='''
            <script type='text/javascript'>
              alert('아이디 또는 패스워드를 확인해주세요!!');
              history.go(-1);
            </script>  
        '''
    return HttpResponse(rs_msg)

def radioButtonView(request) :
    return render(request,
                  'frontapp/js/03_radioButton.html',
                  {})
##라디오버튼 데이터 처리
def jsRadio(request):
    if request.method=='POST':
        #p_city = request.post['city']
       if request.POST.get('city') is not None:
           p_city = request.POST.get('city')
       else :
            rs_msg='''
                 <script type='text/javascript'>
                   alert('잘못된 접근입니다!!');
                   history.go(-1);
                </script>  
            '''
            return HttpResponse(rs_msg)
            
    elif request.method=='GET':  
       if request.GET.get('city') !='' :      
        #p_city = request.GET['city']
           p_city = request.GET.get('city')
       else :
            rs_msg='''
                 <script type='text/javascript'>
                   alert('잘못된 접근입니다!!');
                   history.go(-1);
                  </script>  
                '''
            return HttpResponse(rs_msg)   
    return HttpResponse(p_city)

def jsRadio(request):
    try:
       if request.method=='POST':
           p_city = request.post['city']
           #p_city = request.POST.get('city')                   
       elif request.method=='GET':  
           if request.POST.get('city') is not None:
               p_city = request.POST.get('city')
           else :
               rs_msg='''
                 <script type='text/javascript'>
                   alert('잘못된 접근입니다!!');
                   history.go(-1);
                </script>  
            '''
               return HttpResponse(rs_msg) 
    except :
        rs_msg='''
                 <script type='text/javascript'>
                   alert('잘못된 접근입니다!!');
                   history.go(-1);
                  </script>  
                '''    
        return HttpResponse(rs_msg)   
    return HttpResponse(p_city)
def checkBoxView(request) :
    return render(request,
                  'frontapp/js/05_checkBox.html',
                  {})