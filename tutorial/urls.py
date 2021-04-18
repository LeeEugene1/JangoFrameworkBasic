#유저들이 접근할수있는 URL
"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path

# 2.write 관련 -> 3.view로 이동
from community.views import *
#dfd

urlpatterns = [
    path('admin/', admin.site.urls),
#1.유저접근주소만들기 name은 내부적으로 사용하는 요소?
    # view는 num을 인자값으로 받아야해 정규식이 들어감
    path('write/', write, name = 'write'),
    path('list/', list, name='list'),
    re_path('view/(?P<num>[0-9]+)/$', view),
    # path('<int:view>/', view),
]
