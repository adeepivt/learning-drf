from django.shortcuts import render, HttpResponse
from .models import Bookmark, Tag
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import BookmarkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status


class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        data = request.data
        tag = data.get('tag')
        if tag:
            try:
                title = Tag.objects.get(title=tag)
            except:
                title = Tag.objects.create(title=tag.lower())
                tag = title
            else:
                tag = title
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
