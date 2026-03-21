from rest_framework import serializers
from movies.serializer import MovieSerializer
from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    movie_data = MovieSerializer(source='movie', read_only=True)
    class Meta:
        model = Session
        fields = [
            'id', 
            'movie_data', 
            'start_time', 
            'end_time', 
            'room_number', 
            'created_at', 
            'updated_at'
        ]
