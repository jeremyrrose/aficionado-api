# from django.urls import path, include
from rest_framework import routers
from .views import CreatorProfileViewSet, ImageViewSet, CustomerProfileViewSet, CreatorImages, TagCreators
from django.conf.urls import url

# Should I import TagViewSet as well???


router = routers.DefaultRouter()
router.register('creators', CreatorProfileViewSet, basename='creators')
router.register('customers', CustomerProfileViewSet, basename='customers')
router.register('images', ImageViewSet, basename='images')

custom_urlpatterns = [
    url(r'creators/(?P<creator_pk>\d+)/photos$', CreatorImages.as_view(),
        name='creator_images'),
    url(r'tags/(?P<tag_pk>\d+)/$', TagCreators.as_view(), name='creators_by_tag')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
