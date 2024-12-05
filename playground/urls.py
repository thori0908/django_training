from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello.show),
    path('questions/<int:id>/', views.question.ShowView.as_view()),
]