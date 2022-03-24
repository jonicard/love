
from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import loader, RequestContext


def index(request):
    
    latest_questions=Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context={'latest_questions':latest_questions}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question=Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
    
def results(request, question_id):
    return HttpResponse("Hello, world%s" % question_id)

def vote(request, question_id):
    return HttpResponse("Hello, world%s" % 
question_id)