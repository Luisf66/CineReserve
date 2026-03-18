from rest_framework import generics
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from .serializer import UserSerializer
from .models import User

# Create your views here.
@extend_schema(tags=["Users"])
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=["Users"])
class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]