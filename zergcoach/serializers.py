from rest_framework import serializers
from .models import BuildOrder, Comment
from django.contrib.auth.models import User
from rest_framework import serializers
import logging

class BuildOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildOrder
        fields = ('id', 'title', 'description', 'buildorder','matchup', 'imgur_link')

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'build_order', 'user', 'content', 'username')




logger = logging.getLogger(__name__)



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        logger.info(f"validated_data: {validated_data}")
        try:
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise

