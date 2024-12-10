from django.shortcuts import render
from rest_framework import generics, status
from django.http import HttpResponse
from rest_framework.response import Response
from playground.models import Question
from training.serializers import QuestionSerializer

def show(request) -> HttpResponse:
    return render(request = request, template_name='hello.html',context={'message': 'hello'})
    

