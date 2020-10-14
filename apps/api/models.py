from django.db import models
from apps.authentication.models import User


# Create your models here.

class Tag(models.Model):
    class Meta:
        verbose_name_plural = 'tags'

    tag_name = models.CharField(max_length=500)

    def __str__(self):
        return self.tag_name


class CreatorProfile(models.Model):
    class Meta:
        verbose_name_plural = 'creator_profiles'

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="creators")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    class Meta:
        verbose_name_plural = 'images'

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=500)
    creator_profile = models.ForeignKey(CreatorProfile, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CustomerProfile(models.Model):
    class Meta:
        verbose_name_plural = 'customer_profiles'

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prospect_list = models.ManyToManyField(CreatorProfile, related_name='supporters', blank=True)

    def __str__(self):
        return self.name
