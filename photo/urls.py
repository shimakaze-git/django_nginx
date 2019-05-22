from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.photo_list, name='photo_list'),

    path('<uuid:photo_name>.png/', views.photo_detail, name='photo_detail'),
    path('<uuid:photo_name>.jpg/', views.photo_detail, name='photo_detail'),
]
