from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BuildOrderSerializer, CommentSerializer
from .models import BuildOrder, Comment

# Create your views here.

class BuildOrderView(viewsets.ModelViewSet):
    serializer_class = BuildOrderSerializer
    queryset = BuildOrder.objects.all()

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
