from rest_framework import serializers
from .models import Lcapi, Images


class LcapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lcapi
        fields = ('__all__')

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('__all__')
