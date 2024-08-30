from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnswerSerializer
from .models import Answer

# Create your views here.
class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer