from cProfile import Profile
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, Request, Response, status
from users.models import User
from django.contrib.auth import authenticate
from users.permissions import Authenticated, IsAdminOrReadOnly, IsProfileOwner
from rest_framework.authtoken.models import Token

from users.serializers import LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class UserView(APIView):
    def get(self, request: Request) -> Response:
        accounts = User.objects.all()
        serializer = UserSerializer(accounts, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request: Request): 
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        user_login = authenticate(
            username = serializer.validated_data["username"],
            password = serializer.validated_data["password"],
        )
        if user_login:     
            refresh = RefreshToken.for_user(user_login)            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status.HTTP_200_OK)  
        
        return Response(
            {"detail": "No active account found with the given credentials"}, status.HTTP_401_UNAUTHORIZED)

          
         

class UserDetailView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsProfileOwner]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)
        
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)