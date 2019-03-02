from django.db import models
# reverse() 함수는 URL 패턴을 만들어주는 장고 내장 함수
from django.core.urlresolvers import reverse
# ThumbnailImageField 클래스는 사진 원본 및 썸네일 이미지를 저장하는
# (fields.py 파일에서 정의할) 커스텀 필드 - DISQUS와 다르게 직접 코딩 및 정의해야 함
from dlivry.fields import ThumbnailImageField
from pytz import timezone  # 시간대 처리
from django.utils import timezone


class Album(models.Model):
	name = models.CharField('제품 카테고리', max_length=50)
	description = models.CharField('카테고리 설명', max_length=100, blank=True)

	class Meta:
		ordering = ['name']  # 순서 지정: -name으로 지정하면 최신순 정렬!!!!!!!!!!!!!!!!!

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# 이 메소드가 정의된 객체의 URL /photo/album/99 형식의 값을 반환
		return reverse('dlivry:album_detail', args=(self.id,))  # 사진 번호 url


class Photo(models.Model):
	# 자신의 부모(Album)에 대한 외래키
	album = models.ForeignKey(Album)  # Album부모 테이블에서 참조!
	title = models.CharField('제목', max_length=50)
	image = ThumbnailImageField(upload_to='photo/%Y/%m')  # media 폴더의 photo안에 Y 년도에 해당하는 폴더 \ m 날짜에 해당하는 폴더에 저장함!
	description = models.TextField('제품 설명', blank=True)  # 여러 줄로 작성할 수 있는 게 TextField
	price = models.CharField('가격', max_length=50, null=True)
	upload_date = models.DateTimeField('등록 일시', auto_now_add=True)
	category = models.CharField('카테고리명', max_length=50, null=True)

	dliv_price = models.CharField('배송비', max_length=50, null=True)
	buy = models.CharField('구매혜택', max_length=50, null=True)
	buy_limit = models.CharField('구매제한', max_length=50, null=True)
	# # ##############아래와 같이 속성 처리를 변경해야 한국 시각으로 처리됨#################
	# @property
	# def created_at_korean_time(self):
	# 	korean_timezone = timezone(settings.TIME_ZONE)
	# 	return self.created_at.astimezone(korean_timezone)


	# class Meta:
	# 	ordering = ['title']
	class Meta:  # 날짜 정렬
		ordering = ['upload_date']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# 이 메소드가 정의된 객체의 URL /photo/photo/99 형식의 값을 반환
		return reverse('dlivry:photo_detail', args=(self.id,))

	def get_previous_post(self):  # 3.2.5 항에서 템플릿 작성할 때 사용
		return self.get_previous_by_upload_date()

	def get_next_post(self):  # 3.2.5 항에서 템플릿 작성할 때 사용
		return self.get_next_by_upload_date()

	def get_newer_photo(self):  						# ch10_nav
		newer_photo = Photo.objects.filter(
			upload_date__gt = self.upload_date
			, album = self.album
		).order_by('upload_date').first()
		return newer_photo

	def get_older_photo(self):      					# ch10_nav
		older_photo = Photo.objects.filter(
			upload_date__lt = self.upload_date
			, album = self.album
		).order_by('-upload_date').first()
		return older_photo
