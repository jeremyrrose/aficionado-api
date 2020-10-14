from django.contrib import admin
from .models import Tag, CreatorProfile, Image, CustomerProfile

# Register your models here.
admin.site.register(Tag)
admin.site.register(CreatorProfile)
admin.site.register(Image)
admin.site.register(CustomerProfile)


