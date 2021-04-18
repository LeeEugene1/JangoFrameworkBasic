from django.shortcuts import render
from community.forms import *

# 1. write에서 html파일로 보낸다는 뜻?
# 2. template폴더를 만든뒤 write.html파일을 생성한다.
# def write(request):
#     return render(request, 'write.html')

#1. form.py에서 만든 폼을 적용하기위해 form = form()추가
#2. from community.forms import *
#3. "전달하고자하는애":변수명(form) 집어넣기 -> write라는 html에 form 데이터가 전달된다.
#4. write.html로 이동해보자
# def write(request):
#     form = Form()
#     return render(request, 'write.html', {'form':form})

#1.method방법 입력 만약폼이 유효하면 디비에 저장하고 아니면 그냥 폼만 html에 띄워줘
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    
    return render(request, 'write.html', {'form':form})

    #리스트 리퀘스트를 받아 list.html에 보낸다.
# def list(request):
#     return render(request, 'list.html')

    #html을체우고 다시 여기로돌아와서
    #아티클을 불러오면 아티클에 있는 모든 데이터 컬럼을 가져올수있다. 32쪽
def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})

def view(request, num = "1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html',{'article':article})

