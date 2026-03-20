from django.db.models import ProtectedError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .serializer import SessionSerializer
from .models import Session

# Create your views here.
@extend_schema(tags=["Sessions"])
class SessionListCreateView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=["Sessions"])
class SessionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response(
                {"detail": "Essa sessão possui reservas vinculadas"}, 
                status=status.HTTP_409_CONFLICT
            )

@extend_schema(tags=["Sessions"])
class MovieSessionsListView(generics.ListAPIView):
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Session.objects.filter(movie_id=movie_id)