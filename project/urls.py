"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as core_views


urlpatterns = [
    path('', core_views.home, name="home"),
    path('core/', core_views.list_questions, name='list_questions'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('core/add/', core_views.add_question, name='add_question'),
    path('accounts/profile/', core_views.profile, name='profile'),
    path('core/<int:pk>/', core_views.show_question, name='show_question'),
    path('core/<int:pk>/add_answer', core_views.add_answer, name='add_answer'),
    path('core/<int:pk>/delete/', core_views.delete_question, name='delete_question'),
    path('core/<int:question_pk>/starred/', core_views.toggle_starred_questions, name='toggle_starred_questions'),
    path('answers/<int:answer_pk>/starred/', core_views.toggle_starred_answers, name='toggle_starred_answers'),
    path('core/search/', core_views.search_questions, name='search_questions'),
    path('accept_answer/<int:answer_pk>/', core_views.accept_answer, name='accept_answer')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
