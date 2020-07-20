from django.db import models
from users.models import User
from django.db.models import Q


# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)    
    starred_by = models.ManyToManyField(User, related_name="starred_questions", blank=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    starred_by = models.ManyToManyField(User, related_name="starred_answers", blank=True)
    accepted = models.BooleanField(default=False)

def get_available_questions_for_user(queryset, user):
    if user.is_authenticated:
        questions = queryset.filter(Q(public=True) | Q(author=user))
    else:
        questions = queryset.filter(public=True)
    return questions