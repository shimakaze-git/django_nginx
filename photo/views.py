from .models import Photo
from django.http import HttpResponse
from django.http.response import JsonResponse


def photo_list(request):
    photos = Photo.objects.order_by('uploaded_date')
    url_path = '/photo/'

    photo_dict = {
        str(photo.pk):
        url_path + str(photo.image).replace('photos/', '')
        for photo in photos
    }
    response = JsonResponse(photo_dict)
    return response


def photo_detail(request, photo_name):
    photo_name = str(photo_name)
    uuid = photo_name.split('.')[0]
    photo = Photo.objects.filter(id=uuid).first()
    print("photo : ", photo)

    if photo:
        response = HttpResponse(status=200)

        response["Content-Type"] = "image/png"
        response["Content-Disposition"] = "inline; filename={0}".format(
            photo_name)
        response['X-Accel-Redirect'] = "/media/{0}".format(photo.image)

        return response
    else:
        response = HttpResponse(status=400)
        return response
