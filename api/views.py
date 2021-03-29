from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.serializers import ContentSerializer
from content.models import Content


class ContentList(generics.ListAPIView):
    """View for to display all records."""
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]
