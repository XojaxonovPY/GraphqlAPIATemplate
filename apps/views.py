from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.serializer import ImageSerializer


class ImageGenericApiView(GenericAPIView):
    serializer_class = ImageSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance=serializer.save()
        image_url=request.build_absolute_uri(instance.image.url)
        return Response({'url':image_url})