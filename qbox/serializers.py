from rest_framework import serializers
from core.models import Question, Answer
from users.models import User

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


