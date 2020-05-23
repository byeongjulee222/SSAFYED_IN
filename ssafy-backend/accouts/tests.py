from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserNameSerializer
from .models import User
from rest_framework import generics

# Create your views here.
@api_view(['GET'])
def user_detail(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_name(request):
    user = User.objects.all()
    serializer = UserNameSerializer(user, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def signup(request):
#     serializer = UserSignupSerializer(request.POST)
#     if serializer.is_valid():
#         new_user = User.objects.create_user(**serializer.cleaned_data)
#         login(request, new_user)
#         return Response(serializer.data)
#     else:
#         return HttpResponse('사용자명이 이미 존재합니다.')

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
