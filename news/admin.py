from django.contrib import admin

from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display  = ('title', 'url')

admin.site.register(News, NewsAdmin)
