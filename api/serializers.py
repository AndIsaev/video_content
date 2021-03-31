from rest_framework import serializers
from content.models import Content


class ContentSerializer(serializers.ModelSerializer):
    """Serializer for model Content."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Content
        fields = '__all__'
