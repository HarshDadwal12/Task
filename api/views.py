from django.shortcuts import render, redirect
from .models import Quizzes, Answer
from .serializers import QuizzesSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

class QuizzCRUD(viewsets.ModelViewSet):
    queryset=Quizzes.objects.all()
    serializer_class=QuizzesSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

def well(request):
    return render(request,'welcome.html')

def all_questions(request):
    questions=Quizzes.objects.all()
    return render(request,'index.html',{'questions':questions})

def single_ans(request):
    if request.method == "POST":
        val=request.POST.get('ans')
        choice=Answer(user_answer=val)
        choice.save()
    return redirect('/start')

def mcq_ans(request):
    if request.method=="POST":
        val=request.POST.get('ansm')
        choice=Answer(user_answer=val)
        choice.save()
    return redirect('/start')
    