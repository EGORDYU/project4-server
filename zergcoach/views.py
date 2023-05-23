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
from django.contrib.auth import get_user_model




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



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve and return the user profile data
        user = request.user
        profile_data = {
            'user_id': user.id,  # Include the user_id field
            'username': user.username,
            # Include other profile data fields as needed
        }
        return Response(profile_data)

    

class TokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                access_token = str(token.access_token)
                refresh_token = str(token)
                user_id = token['user_id']  # Assuming the user ID is stored in the token payload
                user = get_user_model().objects.get(pk=user_id)
                username = user.username
                # Other token refresh logic if needed

                return Response({
                    'access': access_token,
                    'refresh': refresh_token,
                    'user_id': user_id,
                    'username': username,  # Include the user ID in the response
                })
            except:
                # Token refresh error handling
                pass
        
        return Response(status=400)