from rest_framework import serializers
from .models import BuildOrder, Comment

class BuildOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildOrder
        fields = ('id', 'title', 'description')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'build_order', 'user', 'content')
