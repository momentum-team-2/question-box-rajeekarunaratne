from rest_framework import serializers
from core.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = Question
        fields = ['id', 'author', 'title', 'body']


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    question = serializers.ReadOnlyField(source="question.title")    
    class Meta:
        model = Answer
        fields = ['id', 'question', 'author', 'body']


# class QuestionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
#     title = serializers.CharField(max_length=255)
#     body = serializers.TextField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Question` instance, given the validated data.
#         """
#         return Question.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Question` instance, given the validated data.
#         """        
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.body = validated_data.get('body', instance.body)
#         instance.save()
#         return instance