from rest_framework import serializers
from .models import Article



class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)

    def create(self, validate_data):
        return Article.objects.create(validate_data)
    

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.description = validate_data.get('description', instance.description)