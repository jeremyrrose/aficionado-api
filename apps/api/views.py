# from django.shortcuts import render
from rest_framework import generics
# from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Tag, CreatorProfile, Image, CustomerProfile
from .serializers import TagSerializer, CreatorProfileSerializer, ImageSerializer, CustomerProfileSerializer


# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer

    def get_queryset(self):
        # a retrieve
        queryset = Tag.objects.all()
        return queryset


class CreatorProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreatorProfileSerializer

    def get_queryset(self):
        queryset = CreatorProfile.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create photographer profiles"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        profile = CreatorProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.owner:
            raise PermissionDenied(
                "You have no permissions to delete this photographer profile"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        profile = CreatorProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == profile.owner:
            raise PermissionDenied(
                "You have no permissions to edit this photographer profile"
            )
        return super().update(request, *args, **kwargs)


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer

    def get_queryset(self):
        queryset = Image.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create photos"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        image = Image.objects.get(pk=self.kwargs["pk"])
        if not request.user == image.owner:
            raise PermissionDenied(
                "You have no permissions to delete this photo"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        image = Image.objects.get(pk=self.kwargs["pk"])
        if not request.user == image.owner:
            raise PermissionDenied(
                "You have no permissions to edit this photo"
            )
        return super().update(request, *args, **kwargs)


class CustomerProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerProfileSerializer

    def get_queryset(self):
        queryset = CustomerProfile.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create customer profiles"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        customer = CustomerProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == customer.owner:
            raise PermissionDenied(
                "You have no permissions to delete this customer profile"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        customer = CustomerProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == customer.owner:
            raise PermissionDenied(
                "You have no permissions to edit this customer profile"
            )
        return super().update(request, *args, **kwargs)


class CreatorImages(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer

    def get_queryset(self):
        if self.kwargs.get("creator_pk"):
            creator = CreatorProfile.objects.get(pk=self.kwargs["creator_pk"])
            queryset = Image.objects.filter(
                creator_profile=creator
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagCreators(generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = CreatorProfileSerializer

    def get_queryset(self):
        if self.kwargs.get("tag_pk"):
            tag = Tag.objects.get(pk=self.kwargs['tag_pk'])
            # creators = CreatorProfile.objects.filter(tags__contains=tag)
            creators = tag.creators.all()
            return creators

    def get(self, *args, **kwargs):
        creators = self.get_queryset()
        serializer = self.serializer_class(creators, many=True)
        return Response(serializer.data)
