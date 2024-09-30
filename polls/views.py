from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnswerSerializer,PersonSerializer, QuestionSerializer, ChoiceSerializer
from .models import Answer,Person,Question, Choice

# Create your views here.
class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class PersonsViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoicesViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer