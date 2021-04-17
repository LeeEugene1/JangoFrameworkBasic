#mvc:modal -> view -> db?
#model은 필요한 데이터, 게시물과관련된 클래스를 만든다.
from django.db import models

# Create your models here.
class Article(models.Model):
        name = models.CharField(max_length=50)
        title = models.CharField(max_length=50)
        contents = models.TextField()
        url = models.URLField()
        email = models.EmailField()
        cdate = models.DateTimeField(auto_now_add=True)

#이제 이모델을 데이터모델에 생성해야한다.
#manage.py migrations community(create model Article)
#이걸 DB적용하기:migrate