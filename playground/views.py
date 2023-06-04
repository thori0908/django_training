from django.shortcuts import render
from django.http import HttpResponse

def hello(request) -> HttpResponse:
    return render(request = request, template_name='hello.html',context={'message': 'hello'})