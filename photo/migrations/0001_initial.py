# Generated by Django 2.2.1 on 2019-05-20 08:54

from django.db import migrations, models
import photo.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=photo.models.uploaded_image_path, verbose_name='画像')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True, verbose_name='アップロード日')),
            ],
        ),
    ]