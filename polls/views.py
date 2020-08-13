from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)


	#template = loader.get_template('polls/index.html')
	#context = {
	#	'latest_question_list': latest_question_list,
	#}
	#return HttpResponse(template.render(context, request))
	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)
	
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    #try:
    #	question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #	raise Http404("question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})

    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

