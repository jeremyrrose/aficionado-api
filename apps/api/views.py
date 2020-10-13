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
from .models import Tag, PhotographerProfile, Photo, CustomerProfile
from .serializers import TagSerializer, PhotographerProfileSerializer, PhotoSerializer, CustomerProfileSerializer


# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer

    def get_queryset(self):
        # a retrieve
        queryset = Tag.objects.all()
        return queryset


class PhotographerProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotographerProfileSerializer

    def get_queryset(self):
        queryset = PhotographerProfile.objects.all()
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
        photographer = PhotographerProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == photographer.owner:
            raise PermissionDenied(
                "You have no permissions to delete this photographer profile"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        photographer = PhotographerProfile.objects.get(pk=self.kwargs["pk"])
        if not request.user == photographer.owner:
            raise PermissionDenied(
                "You have no permissions to edit this photographer profile"
            )
        return super().update(request, *args, **kwargs)


class PhotoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = Photo.objects.all()
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
        photo = Photo.objects.get(pk=self.kwargs["pk"])
        if not request.user == photo.owner:
            raise PermissionDenied(
                "You have no permissions to delete this photo"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        photo = Photo.objects.get(pk=self.kwargs["pk"])
        if not request.user == photo.owner:
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


class PhotographerPhotos(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer

    def get_queryset(self):
        if self.kwargs.get("photographer_pk"):
            photographer = PhotographerProfile.objects.get(pk=self.kwargs["photographer_pk"])
            queryset = Photo.objects.filter(
                photographerprofile=photographer
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# class SinglePhotographerPhoto(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = PhotoSerializer
#
#     def get_queryset(self):
#         # localhost:8000/categories/category_pk<1>/recipes/pk<1>/
#         """
#       kwargs = {
#          "photographer_pk": 1,
#          "pk": 1
#       }
#       """
#         if self.kwargs.get("photographer_pk") and self.kwargs.get("pk"):
#             photographer = PhotographerProfile.objects.get(pk=self.kwargs["photographer_pk"])
#             queryset = Photo.objects.filter(
#                 pk=self.kwargs["pk"],
#                 owner=self.request.user,
#                 photographer=photographer)
#             return queryset
#
#
# class PhotoViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = PhotoSerializer
#
#     def get_queryset(self):
#         queryset = Photo.objects.all().filter(owner=self.request.user)
#         return queryset
#
#     def create(self, request, *args, **kwargs):
#         if request.user.is_anonymous:
#             raise PermissionDenied(
#                 "Only logged in users with accounts can create photos"
#             )
#         return super().create(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     def destroy(self, request, *args, **kwargs):
#         photo = Photo.objects.get(pk=self.kwargs["pk"])
#         if not request.user == photo.owner:
#             raise PermissionDenied(
#                 "You have no permissions to delete this photo"
#             )
#         return super().destroy(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         photo = Photo.objects.get(pk=self.kwargs["pk"])
#         if not request.user == photo.owner:
#             raise PermissionDenied(
#                 "You have no permissions to edit this photo"
#             )
#         return super().update(request, *args, **kwargs)


# class CustomerProfileViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CustomerProfileSerializer

# def get_queryset(self):
#     # list all customers per current loggedin user
#     queryset = CustomerProfile.objects.all().filter(owner=self.request.user)
#     return queryset
#
# def create(self, request, *args, **kwargs):
#     # check if customer already exists for current logged in user
#     customer = CustomerProfile.objects.filter(
#         name=request.data.get('name'),
#         owner=request.user
#     )
#     if customer:
#         msg = 'customer with that name already exists'
#         raise ValidationError(msg)
#     return super().create(request)
#
# def perform_create(self, serializer):
#     serializer.save(owner=self.request.user)
#
# # user can only delete customer he/she created
# def destroy(self, request, *args, **kwargs):
#     customer = CustomerProfile.objects.get(pk=self.kwargs["pk"])
#     if not request.user == customer.owner:
#         raise PermissionDenied("You can not delete this customer")
#     return super().destroy(request, *args, **kwargs)
