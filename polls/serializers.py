from rest_framework import serializers
from .models import Answer, Person, Choice, Question

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ['id', 'name', 'age']

class ChoiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Choice
    fields = ['id', 'choice_text', 'question']

class QuestionSerializer(serializers.ModelSerializer):
  choices = ChoiceSerializer(read_only=True, many=True)
  class Meta:
    model = Question
    fields = ['id', 'question_text','pub_date', 'choices']

class AnswerSerializer(serializers.ModelSerializer):
  person = serializers.RelatedField(read_only=True, many=True)
  choice = serializers.RelatedField(read_only=True, many=True)

  class Meta:
    model = Answer
    fields = ['id','person', 'choice']

