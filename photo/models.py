from uuid import uuid4
from django.db import models


def uploaded_image_path(instance, filename):
    # アップロード先：MEDIA_ROOT/photos/<uuid>.png
    image_extension = filename.split('.')[-1]
    return f'photos/{instance.id}.{image_extension}'


class Photo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    image = models.ImageField('画像', upload_to=uploaded_image_path)
    uploaded_date = models.DateTimeField('アップロード日', auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
