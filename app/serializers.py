from rest_framework import serializers
from .models import Fasteignakaup

class FasteignakaupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fasteignakaup
        fields = '__all__'