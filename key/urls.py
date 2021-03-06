"""key URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from keyapi.views import login_user, register_user, KeyUserView, ProjectView, FieldView
from keyapi.views.institution import InstitutionView
from keyapi.views.interview import InterviewView
from keyapi.views.interview_question import InterviewQuestionView
from keyapi.views.question import QuestionView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', KeyUserView, 'key user')
router.register(r'projects', ProjectView, 'project')
router.register(r'fields', FieldView, 'field')
router.register(r'interviews', InterviewView, 'interview')
router.register(r'questions', QuestionView, 'question')
router.register(r'interviewquestions', InterviewQuestionView, 'interviewquestion')
router.register(r'institutions', InstitutionView, 'institution')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
