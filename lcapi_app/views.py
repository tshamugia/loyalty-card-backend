"""Module Export"""
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Lcapi, Images
from .serializer import LcapiSerializer, ImagesSerializer


class LcapiViewSet(viewsets.ModelViewSet):
    serializer_class = LcapiSerializer

    def get_object(self,  **kwargs):
        card_id = self.kwargs.get('pk')
        return get_object_or_404(Lcapi, card_id=card_id)

    def get_queryset(self):
        return Lcapi.objects.all()  # pylint: disable=maybe-no-member

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer