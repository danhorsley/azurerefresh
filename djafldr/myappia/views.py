from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Sum, Max, Min
from datetime import datetime, timedelta
from .models import DailyData
from .plots import *
import plotly.graph_objects as go
import plotly.offline as py
import numpy as np

#utility function to convert datetime into dates
def filter_hist(my_date):
    return datetime.strptime(my_date, '%Y-%m-%d %H:%M:%S+00:00').date() 

def dmy(eff):
    return f'{eff.year}-{eff.month:02d}-{eff.day:02d}'


def index(request):
    return HttpResponse("Hello everyone. My app is live")

def query2(request):
    
    try:
        if request.POST['timeperiod'] == "all time":
            new_time_period = "all time"
        else:
            new_time_period = f"last {request.POST['timeperiod']}"
        html_plot = sales_over_time_chart(request.POST['measure'], request.POST['timeperiod'],
                                        request.POST['title'], request.POST['timesplit'])
        default_sub = f"{request.POST['timesplit'].capitalize()} {request.POST['measure']} of {request.POST['title']} over {new_time_period}"
    except:
        html_plot = sales_over_time_chart()
        default_sub = "Sales of all titles since inception"

    title = list(set(DailyData.objects.values_list('itemname', flat=True))) #filter1 for title 
    timesplit = ['daily', 'by weekday', 'by week', 'by month']
    time_period = ['all time', '7d', '30d', '90d', '180d'] #filter for time period
    measure = ['quantity', 'net profit'] #quantity or net profit
    title.sort()
    title = ['all titles'] + title
    

    return render(request, 'query2.html', {'titles' : title , 'timesplit' : timesplit ,
                                                'time_period' : time_period,
                                                'measures' : measure,
                                                'html_plot' : html_plot,
                                                "default_sub" : default_sub
                                                })

def homepage(request):
    title1 = list(set(DailyData.objects.values_list('itemname', flat=True))) #filter1 for title 
    timesplit = ['daily', 'by weekday', 'by week', 'by month']
    time_period = ['all time', '7d', '30d', '90d', '180d'] #filter for time period
    measure = ['quantity', 'net profit'] #quantity or net profit
    title1.sort()
    title1 = ['all titles'] + title1
    

    return render(request, 'query.html', {'titles1' : title1 , 'timesplit' : timesplit ,
                                                'time_period' : time_period,
                                                'measures' :measure
                                                })
def answer(request):
    title1 = request.POST['title1']
    timesplit = request.POST['timesplit']
    measure = request.POST['measure']
    timeperiod = request.POST['timeperiod']
    
    html_plot = sales_over_time_chart(measure, timeperiod, title1, timesplit)
    return render(request, 'answer.html', {'sales_chart' : html_plot})
    

