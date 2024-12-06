from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from playground.models import Question
from training.serializers import QuestionSerializer
from drf_yasg.utils import swagger_auto_schema

class ShowView(APIView):
    @swagger_auto_schema(
        responses={200: QuestionSerializer()}
    )
    def get(self, request, *args, **kwargs) -> Response:
        id = kwargs.get('id')
        question = Question(id=id, question_text='What is the meaning of life?', pub_date='2022-01-01')
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
