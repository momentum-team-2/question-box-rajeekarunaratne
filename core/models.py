from django.db import models
from users.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    starred_by = models.ManyToManyField(User, related_name="starred_questions")

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    starred_by = models.ManyToManyField(User, related_name="starred_answers")
