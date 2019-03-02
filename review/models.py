from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    rating = models.CharField(max_length=30, null=True)
    product = models.CharField(max_length=30, null=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = '자랑'

    def __str__(self):
        return self.title


