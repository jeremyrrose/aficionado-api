from django.contrib import admin
from .models import Tag, PhotographerProfile, Photo, CustomerProfile

# Register your models here.
admin.site.register(Tag)
admin.site.register(PhotographerProfile)
admin.site.register(Photo)
admin.site.register(CustomerProfile)


