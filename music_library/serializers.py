from dataclasses import fields
from rest_framework import serializers
from .models import Music_Library

class Music_LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_Library
        fields = ['id', 'title', 'artist', 'release_date', 'genre']