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
from rest_framework import generics
from .serializers import FavoriteSerializer
from .serializers import Favorite
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import BuildOrderSerializer, CommentSerializer
from .models import BuildOrder, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




class BuildOrderView(viewsets.ModelViewSet):
    serializer_class = BuildOrderSerializer
    queryset = BuildOrder.objects.all()

class CommentView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow authenticated users to create comments

    def get_queryset(self):
        queryset = Comment.objects.all()
        build_order_id = self.request.query_params.get('build_order', None)
        if build_order_id is not None:
            queryset = queryset.filter(build_order_id=build_order_id)
        return queryset

class HomeView(APIView):   
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

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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

class FavoriteView(generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add the IsAuthenticated permission

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Associate the favorite with the authenticated user

class DeleteFavoriteView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add the IsAuthenticated permission

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(
            user=self.request.user,
            build_order_id=self.kwargs['build_order_id']
        )
        return obj

class UserFavoritesView(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Favorite.objects.filter(user_id=user_id)
        else:
            return Favorite.objects.all()

class BuildDetailView(APIView):
    def get(self, request, build_id):
        try:
            build = BuildOrder.objects.get(id=build_id)
            serializer = BuildOrderSerializer(build)
            return Response(serializer.data)
        except BuildOrder.DoesNotExist:
            return Response({'error': 'Build not found'}, status=status.HTTP_404_NOT_FOUND)