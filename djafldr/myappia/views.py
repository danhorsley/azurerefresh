from django.shortcuts import render
from .models import DailyData

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello everyone. My app is live")

def homepage(request):
    title1 = list(set(DailyData.objects.values_list('itemname', flat=True))) #filter1 for title 
    title2 = [] #filter2 for title
    time_period = [] #filter for time period
    measure = [] #quantity or net profit
    title1.sort()
    title1 = ['all titles'] + title1

    return render(request, 'query.html', {'titles1' : title1 , 'titles2' : title2 ,
                                                'time_period' : time_period,
                                                'measures' :measure
                                                })
def answer(request):
    title1 = request.POST['title1']
    return HttpResponse("answer place holder")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
