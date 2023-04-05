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
    ###http://127.0.0.1:8000/main/main
    # path("main/", views.main),
    path('',views.index),
    path("index/", views.index),
    # path('main/main/',views.main),
    path('image/',views.imageView), 
    path('css_1/',views.cssView1), 
    path('css_2/',views.cssView2), 
    path('css_3/',views.cssView3), 
    path('javascript1/',views.cssView4),
    path('javascript2/',views.cssView5),  
    path('javascript3/',views.cssView6),  
    path('01_html/',views.htmlview01),  
    path('02_link/',views.linkview),  
    path('03_link/',views.linkview2),  
    path('04_css/',views.cssview),  
    path('05_table/',views.tableview),  
    path('06_table/',views.tableview2),  
    path('07_ul/',views.ulview),  
    path('08_div/',views.ulview1),  
    path('09_div/',views.divview2),  
    path('10_iframe/',views.iframeview),  
    path('01_table/',views.cssTableview)  
    
]

