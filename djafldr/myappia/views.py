from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Sum
from datetime import datetime
from .models import DailyData
import plotly.graph_objects as go
import plotly.offline as py
import numpy as np

#utility function to convert datetime into dates
def filter_hist(my_date):
    return datetime.strptime(my_date, '%Y-%m-%d %H:%M:%S+00:00').date() 


def index(request):
    return HttpResponse("Hello everyone. My app is live")

def homepage(request):
    title1 = list(set(DailyData.objects.values_list('itemname', flat=True))) #filter1 for title 
    title2 = list(set(DailyData.objects.values_list('itemname', flat=True))) #filter2 for title
    time_period = ['all time', '30d', '90d', '180d'] #filter for time period
    measure = ['quantity', 'net profit'] #quantity or net profit
    title1.sort()
    title1 = ['all titles'] + title1
    title2 = ['all titles'] + title2
    

    return render(request, 'query.html', {'titles1' : title1 , 'titles2' : title2 ,
                                                'time_period' : time_period,
                                                'measures' :measure
                                                })
def answer(request):
    title1 = request.POST['title1']
    title2 = request.POST['title2']
    measure = request.POST['measure']
    timeperiod = request.POST['timeperiod']
    #print(title1)
    
    my_filter = DailyData.objects.filter(itemname__contains = title1)\
                                    .values('date').order_by('date')\
                                    .annotate(total_profit= Sum('net_profit')).values_list()
    print(my_filter[0])
    my_array = np.core.records.fromrecords(my_filter, 
                                    names=[f.name for f in DailyData._meta.fields]+['total_profit'])
    my_dates = [x.date() for x in my_array['date']]
    my_plot = go.Figure(data=[go.Bar(x=my_dates, y=my_array['total_profit'])],
                        layout_title_text=f"sales of {title1[:20]} over time"
                        )
    my_plot.update_layout(
    autosize=False,
    width=1000,
    height=618,
    legend_orientation="h",
    #legend=dict(x=0, y=-0.4),
    yaxis=go.layout.YAxis(
        titlefont=dict(size=15),
        tickformat=",.1%"
        )
    )
    html_plot = py.plot(my_plot, output_type ='div')
    return render(request, 'answer.html', {'sales_chart' : html_plot})
    # return HttpResponse(f"""answer place holder : {title1}, {title2}, 
    #                         {measure}, {timeperiod}, {html_plot}""")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
