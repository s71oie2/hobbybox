from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse
from .fields import ThumbnailImageField

class News(models.Model):
    image = ThumbnailImageField(upload_to='news/%Y/%m', null=True)
    title = models.CharField('제목',max_length=50, blank=True, null=True)
    content= models.TextField('내용', max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    create_date = models.DateTimeField('작성일', auto_now_add=True) # 작성일 자동생성

    class Meta:  # 필드 속성 외에 필요한 파라미터를 Meta 내부 클래스로 정의
        verbose_name = '새소식'  # 'post'
        verbose_name_plural = '소식'  # 'posts'
        ordering = ('create_date',)

    def __str__(self):
        return self.title

