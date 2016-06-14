from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Question, Choice

def index(request):
    # return HttpResponse("Hello Train the Trainer Class")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'training_evaluation/index.html', context=context)

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request, 'training_evaluation/detail.html', context=context)


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request, 'training_evaluation/results.html', context=context)


def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = Question.objects.get(pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('results', args=(question.id,)))
