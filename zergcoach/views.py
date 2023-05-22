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

    def get_queryset(self):
        """
        Optionally restricts the returned comments to a given build_order,
        by filtering against a `build_order` query parameter in the URL.
        """
        queryset = Comment.objects.all()
        build_order_id = self.request.query_params.get('build_order', None)
        if build_order_id is not None:
            queryset = queryset.filter(build_order_id=build_order_id)
        return queryset
