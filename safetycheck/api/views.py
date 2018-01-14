from django.shortcuts import render
from django.contrib.auth.models import User
from .serelizers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions
from  rest_framework.response import Response
from  rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.
class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    def post(self,request):

        email_address = request.data.get('email')
        user_request = get_object_or_404(
            User,
            email=email_address,
        )
        username = user_request.username

        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

class user_bac_view(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
                          ]

    def post(self,request):
        serializer = user_bacserelizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(serializer.data)

    def get(self,request):
        ser = user_bac_video.objects.filter(user = self.request.user)
        serializer = user_bacserelizer(ser,many=True)

        return Response(serializer.data)
