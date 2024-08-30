from rest_framework import serializers
from .models import Answer, Person, Choice

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ['id', 'name', 'age']


class ChoiceSerializer(serializers.ModelSerializer):
  question = serializers.RelatedField(read_only=True)
  class Meta:
    model = Choice
    fields = ['id', 'choice_text', 'question']


class AnswerSerializer(serializers.ModelSerializer):
  person = serializers.RelatedField(read_only=True, many=True)
  choice = serializers.RelatedField(read_only=True, many=True)

  class Meta:
    model = Answer
    fields = ['id','person', 'choice']

