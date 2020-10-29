from .models import Film
from rest_framework import serializers


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'description']