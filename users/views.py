from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from utils.generic_set_views import ListCreateGenericView, RetrieveUpdateDeleteGenericView
from rest_framework import generics
class UserView(ListCreateGenericView):
    view_queryset = User.objects.all()
    view_serializer = UserSerializer
  

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
