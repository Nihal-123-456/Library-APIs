from rest_framework import serializers
from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(many=False)
    reviewer = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'