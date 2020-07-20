from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Answer, Question, get_available_questions_for_user
from .forms import AnswerForm, QuestionForm
from users.models import User
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.postgres.search import SearchVector

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('list_questions') 
    return render(request, 'core/home.html')

@login_required
def list_questions(request):
    questions = get_available_questions_for_user(Question.objects,
                                             request.user).order_by('title')
    return render(request, 'core/list_questions.html', {'questions': questions})

@login_required
def show_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    form = QuestionForm()
    answers = question.answers.order_by('date_added')
    user_favorite = request.user.is_starred_questions(question)
    return render(request, 'core/show_question.html', {'question': question, 'pk': pk, 'form': form, 'answers': answers, 'user_favorite': user_favorite})

def add_question(request):
    if request.method == 'GET':
        form = QuestionForm()
    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.instance
            question.author = request.user
            question.save()
            return redirect(to='list_questions')

    return render(request, 'core/add_question.html', {'form': form})

@login_required
@csrf_exempt
@require_POST
def toggle_starred_questions(request, question_pk):    
    question = get_object_or_404(get_available_questions_for_user(
        Question.objects, request.user),
                               pk=question_pk)

    if question in request.user.starred_questions.all():
        request.user.starred_questions.remove(question)
        return JsonResponse({"starred": False})
    else:
        request.user.starred_questions.add(question)
        return JsonResponse({"starred": True})


@login_required
@csrf_exempt
@require_POST
def toggle_starred_answers(request, answer_pk):    
    answer = get_object_or_404(Answer, pk=answer_pk)

    if answer in request.user.starred_answers.all():
        request.user.starred_answers.remove(answer)
        return JsonResponse({"starred": False})
    else:
        request.user.starred_answers.add(answer)
        return JsonResponse({"starred": True})

def profile (request):
    return render(request, 'core/profile.html')


def add_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    # answer = question.answers.order_by('date_added')
    if request.method == 'GET':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.instance
            answer.author = request.user
            answer.question =question
            answer.save()
            return redirect(to='show_question', pk=pk)
    return render(request, 'core/add_answer.html', {'form': form, 'question': question})


@login_required
def delete_question(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect(to='list_questions')

    return render(request, 'core/delete_question.html', {'question': question})


def search_questions(request):
    query = request.GET['q']
    questions = Question.objects.annotate(
        search=SearchVector('body', 'title')).filter(search=query)
    return render(request, 'core/list_questions.html', {'questions': questions})

def accept_answer(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if answer.accepted == False:
        answer.accepted = True
        answer.save()
    else: 
        answer.accepted = False
        answer.save()
    return redirect(to='show_question', pk=answer.question.pk)