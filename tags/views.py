from django.shortcuts import render, HttpResponse
from .models import Bookmark, Tag
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import BookmarkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        tag = serializer.validated_data['tag']
        titles = Tag.objects.all()
        if tag not in titles:
            title = Tag.objects.create(title=tag)
            print(title)
        