from rest_framework import serializers
from core.models import Question, Answer
from users.models import User




class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    question_id = serializers.IntegerField()    
    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'author', 'body']


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'author', 'title', 'body', 'answers']