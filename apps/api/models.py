from django.db import models
from apps.authentication.models import User


# Create your models here.

class Tag(models.Model):
    class Meta:
        verbose_name_plural = 'tags'

    tag_name = models.CharField(max_length=500)

    def __str__(self):
        return self.tag_name


class PhotographerProfile(models.Model):
    class Meta:
        verbose_name_plural = 'photographerprofiles'

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Do I need a photo an array of photos for the class Photo?
class Photo(models.Model):
    class Meta:
        verbose_name_plural = 'photos'

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_url = models.URLField(max_length=500)
    photographerprofile = models.ForeignKey(PhotographerProfile, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CustomerProfile(models.Model):
    class Meta:
        verbose_name_plural = 'customerprofiles'

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prospect_list = models.ManyToManyField(PhotographerProfile, blank=True)

    # class ProspectList(models.Model):
    #
    #     photographer = models.ForeignKey(PhotographerProfile, related_name='recipes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
