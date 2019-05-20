from django.db import models
from django.utils import timezone

from photo.models import Photo


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    photo = models.ForeignKey(
        # 'Photo',
        Photo,
        on_delete=models.PROTECT,
        verbose_name='写真',
        related_name='post',
        blank=True,
        null=True
    )

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
