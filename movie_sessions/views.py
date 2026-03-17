from rest_framework import generics
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from .serializer import SessionSerializer
from .models import Session

# Create your views here.
@extend_schema(tags=["Sessions"])
class SessionListCreateView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=["Sessions"])
class SessionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=["Sessions"])
class MovieSessionsListView(generics.ListAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Session.objects.filter(movie_id=movie_id)