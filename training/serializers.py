from rest_framework import serializers
from playground.models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']


# NOTE: when using serializers.Serializer
# class QuestionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     question_text = serializers.CharField()
#     pub_date = serializers.DateField()
