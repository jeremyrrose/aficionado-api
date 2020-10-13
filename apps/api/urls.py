# from django.urls import path, include
from rest_framework import routers
from .views import PhotographerProfileViewSet, PhotoViewSet, CustomerProfileViewSet, PhotographerPhotos
from django.conf.urls import url

# Should I import TagViewSet as well???


router = routers.DefaultRouter()
router.register('photographers', PhotographerProfileViewSet, basename='photographers')
router.register('customers', CustomerProfileViewSet, basename='customers')
router.register('photos', PhotoViewSet, basename='photos')

custom_urlpatterns = [
    url(r'photographers/(?P<photographer_pk>\d+)/photos$', PhotographerPhotos.as_view(),
        name='photographer_photos')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
