from django.db import models
# reverse() 함수는 URL 패턴을 만들어주는 장고 내장 함수
from django.core.urlresolvers import reverse

# ThumbnailImageField 클래스는 사진 원본 및 썸네일 이미지를 저장하는
# (fields.py 파일에서 정의할) 커스텀 필드 - DISQUS와 다르게 직접 코딩 및 정의해야 함
from hobby.fields import ThumbnailImageField
from pytz import timezone  # 시간대 처리
from django.utils import timezone


class Album(models.Model):
	name = models.CharField('제품 카테고리', max_length=50)
	description = models.CharField('카테고리 설명', max_length=100, blank=True)

	class Meta:
		ordering = ['name']  # 순서 지정

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('hobby:album_detail', args=(self.id,))


class Photo(models.Model):
	# 자신의 부모(Album)에 대한 외래키
	album = models.ForeignKey(Album)  # Album부모 테이블에서 참조!
	title = models.CharField('제목', max_length=50)
	image = ThumbnailImageField(upload_to='hobby/%Y/%m')
	description = models.TextField('제품 설명', blank=True)
	price = models.CharField('가격', max_length=50, null=True)
	curator = models.CharField('큐레이터', max_length=50, null=True)
	dliv_price = models.CharField('배송비', max_length=50, null=True)
	buy = models.CharField('구매혜택', max_length=50, null=True)
	buy_limit = models.CharField('구매제한', max_length=50, null=True)
	# settings.TIME_ZONE = 'Asia/Seoul' 으로 설정해도 UTC 시각으로 처리됨
	# DB에 저장되는 시각은 UTC 시각이지만, 아래 속성 처리로 한국 시각으로 변환하여 템플릿에 제공함

  # upload_date = models.DateTimeField('등록 일시', auto_now_add=True)
	upload_date = models.DateTimeField('등록 일시', auto_now_add=True)

	class Meta:  # 날짜 최신순 정렬
		ordering = ['-upload_date']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# 이 메소드가 정의된 객체의 URL /photo/photo/99 형식의 값을 반환
		return reverse('hobby:photo_detail', args=(self.id,))

