from django.urls import path

### from 뒤에 작성규칙
#폴더 경로 또는 폴더 경로+파일명
### import 뒤에 작성규칙
# *from에서 폴더경로까지만 지정한 경우
#  -파일명
# *from에서 파일명까지 지정한 경우
# -클래스명 또는 함수명


##http://127.0.0.1:8000/url경로/
##path('url경로', 함수이름),

from . import views 

urlpatterns = [
    ###http://127.0.0.1:8000/first/index
    path("", views.index),
    path("index/", views.index),
    path("testpage/", views.testPage),    
]
