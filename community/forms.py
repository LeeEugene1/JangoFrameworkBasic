#1.django.forms에서 ModelForm을 import한다.
from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']

#2.view.py에가서 form = form()을 추가해준다.