from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from review.models import Rating, Comment


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        like = self.Meta.model.objects.create(author=user, **validated_data)
        return like

