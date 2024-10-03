from rest_framework import serializers
from .models import BookModel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'  # Or specify individual fields like ['id', 'name', 'author', 'pages']
