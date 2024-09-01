from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import TokenError
from django.db import transaction

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            refresh_token = response.data['refresh']
            response.set_cookie(
                key='refresh',
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='Strict', 
            )
            del response.data["refresh"]
        return response




class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'email': user.email,
            'username': user.username,
        }, status=status.HTTP_200_OK)

class CustomTokenRefreshView(TokenRefreshView):


    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token not found in cookies'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            user_id = refresh['user_id']
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except TokenError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data={'refresh': refresh_token})
        serializer.is_valid(raise_exception=True)
        
        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        response.set_cookie(
            key='refresh',
            value=refresh_token,
            httponly=True,
            secure=True, 
            samesite='Strict', 
        )
        return response
