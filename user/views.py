from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializer import SignInSerializer, SignUpSerializer, UserSerializer
from user.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .premissions import UserListPermission


class SignUpView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        if CustomUser.objects.filter(
           username=request.data.get('username')).exists():
            return Response('Username already exists!!',
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        token = Token.objects.create(user=user)

        return Response({'data': serializer.data, 'token': token.key},
                        status=status.HTTP_201_CREATED)


class UserLoginView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = SignInSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed("Invalid username or password.")
        token, created = Token.objects.get_or_create(user=user)
        response = {'token': token.key}
        response['is_admin'] = user.is_admin

        return Response(response, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, UserListPermission]
