"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# from mainapp import views
### from 뒤에 작성규칙
#폴더 경로 또는 폴더 경로+파일명
### import 뒤에 작성규칙
# *from에서 폴더경로까지만 지정한 경우
#  -파일명
# *from에서 파일명까지 지정한 경우
# -클래스명 또는 함수명

# from firstapp import views as v1
# from secondapp import views as v2

##http://127.0.0.1:8000/url경로/
##path('url경로', 함수이름),
urlpatterns = [
    ##http://127.0.0.1:8000/second/
    path("", include('mainapp.urls')),
    # path("index/", views.index),
    # path("testpage/", v2.testPage),
    # path("second/", v2.second),
    
    ###http://127.0.0.1:8000/first/testpage
    path('first/', include('firstapp.urls')),
    ###http://127.0.0.1:8000/second/testpage
    path('second/', include('secondapp.urls')),
    ###http://127.0.0.1:8000/main/testpage
    path('main/', include('mainapp.urls')),
    ###http://127.0.0.1:8000/front/testpage
    path('front/', include('frontapp.urls')),

    # path('', include('mainapp.urls')),
    path("admin/", admin.site.urls),
    
]
