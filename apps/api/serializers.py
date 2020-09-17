from rest_framework import serializers
from .models import Tag, PhotographerProfile, Photo, CustomerProfile


# we need to serialize our data so that it's in a format we can use

# questions - are my serializers in the right order?
# for photos, is it read_only or is it something else, perhaps
# view_only?
class CustomerProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CustomerProfile
        fields = ('id', 'name', 'owner', 'email', 'phone', 'image_url', 'created_at',
                  'updated_at', 'prospect_list')


class PhotoSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Photo
        fields = ('id', 'title', 'description', 'photo_url', 'photographerprofile')


class PhotographerProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    photos = PhotoSerializer(many=True, read_only=False, required=False)


    # customerprofiles = CustomerProfileSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = PhotographerProfile
        fields = ('id', 'name', 'owner', 'email', 'phone', 'image_url', 'photos', 'tags',
                  'created_at', 'updated_at')


class TagSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # photographerprofiles = PhotographerProfileSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Tag
        fields = ('tag_name')
#
