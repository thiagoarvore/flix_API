from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None


class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()  # O serializer gênero arruma tudo pro serializer de filme
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None

    #     reviews = obj.reviews.all()
    #     if reviews:
    #         sum_reviews = 0
    #         for review in reviews:
    #             sum_reviews += review.stars
    #         return round(sum_reviews/reviews.count(), 1)
    #     return None
