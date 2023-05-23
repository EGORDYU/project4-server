from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BuildOrderSerializer, CommentSerializer
from .models import BuildOrder, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserCreateSerializer



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

class HomeView(APIView):   
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'Welcome to the JWT  Authentication page using React Js and Django!'}
        return Response(content)
    

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
