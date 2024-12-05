from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from playground.models import Question
from training.serializers import QuestionSerializer

class ShowView(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        id = kwargs.get('id')
        question = Question(id=id, question_text='What is the meaning of life?', pub_date='2022-01-01')
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
