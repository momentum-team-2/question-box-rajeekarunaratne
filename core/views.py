from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Answer, Question
from .forms import AnswerForm, QuestionForm
from users.models import User
from django.views import View

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('list_questions') 
        # must create template above
    return render(request, 'core/home.html')