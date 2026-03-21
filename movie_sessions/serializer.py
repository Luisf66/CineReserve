from rest_framework import serializers
from movies.serializer import MovieSerializer
from .models import Session
from movies.models import Movie

class SessionSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    movie_data = MovieSerializer(source='movie', read_only=True)
    class Meta:
        model = Session
        fields = [
            'id', 
            'movie',
            'movie_data', 
            'start_time', 
            'end_time', 
            'room_number', 
            'created_at', 
            'updated_at'
        ]
