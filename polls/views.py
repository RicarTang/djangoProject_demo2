from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
from django.http import Http404


# from django.template import loader
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # 查询时间最新发布的5个
    # template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)  # render()快捷方式
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context,request))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)  # 简介写法
    return render(request, 'polls/detail.html', {'question': question})




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
