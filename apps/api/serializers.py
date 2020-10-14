from rest_framework import serializers
from .models import Tag, CreatorProfile, Image, CustomerProfile


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


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'title', 'description', 'image_url', 'creator_profile')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'tag_name')


class CreatorProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = ImageSerializer(many=True, read_only=True, required=False)
    supporters = CustomerProfileSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = CreatorProfile
        fields = ('id', 'name', 'owner', 'email', 'phone', 'image_url', 'images', 'tags', 'supporters',
                  'created_at', 'updated_at')
