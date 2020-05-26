from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('image/<cat_name>/(<int:image_id>)',views.single_image, name='image_gallery'),
    path('location/<pic_location>', views.new_location, name='filter_location'),
    path('search', views.search, name='search_images')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)