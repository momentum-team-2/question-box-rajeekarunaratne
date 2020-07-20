from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    def is_starred_questions(self, question):
        return self.starred_questions.filter(pk=question.pk).count() == 1
    
    def is_starred_answers(self, answer):
        return self.starred_answers.filter(pk=answer.pk).count() == 1
