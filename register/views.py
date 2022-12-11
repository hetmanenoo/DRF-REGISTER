from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Register
from .serializers import RegisterSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly



class RegisterAPIList(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class RegisterAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (IsAuthenticated, )

class RegisterAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (IsAdminOrReadOnly,)
