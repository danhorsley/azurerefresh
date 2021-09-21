from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.offline as py
from .models import DailyData
from django.db.models import Count, Sum, Max, Min
from django.db.models.functions import ExtractWeek, ExtractYear, ExtractMonth, ExtractWeekDay
import numpy as np
import calendar


def dmy(eff):
    return f'{eff.year}-{eff.month:02d}-{eff.day:02d}'
def sqldate_to_datetime(my_date):
    return datetime.strptime(my_date, '%Y-%m-%d %H:%M:%S+00:00').date() 

def sales_over_time_chart(measure='net profit', timeperiod = 'all_time', 
                            title1 = '', my_ts = 'daily', cumulative = 'distinct'):
    #print(measure, timeperiod, title1, my_ts)
    time_max = DailyData.objects.values().aggregate(Max('date'))['date__max']
    time_min = DailyData.objects.values().aggregate(Min('date'))['date__min']

    time_dict = {'all_time' : time_max-time_min, 'all time' : time_max-time_min, 
                '7d' : timedelta(days = 50), '30d' : timedelta(days = 30),
                '90d': timedelta(days = 90), '180d': timedelta(days = 180)}
    timeperiod_dict =  {'daily' : 'date', 'by weekday': 'day', 
                        'by week': 'week', 'by month' : 'month'}
    measure_dict = {'quantity' : 'quantity', 'net profit' : 'net_profit'}
    tick_dict = {'quantity' : "d", "net profit" : ".2"}

    
    my_filter = DailyData.objects.filter(itemname__contains = title1,
                                date__range=[dmy(time_max-time_dict[timeperiod]), dmy(time_max)])\
                                .annotate(year=ExtractYear('date'))\
                                .annotate(week=ExtractWeek('date'))\
                                .annotate(month=ExtractMonth('date'))\
                                .annotate(day=ExtractWeekDay('date'))\
                                .values('date', 'day', 'week', 'month', 'year').order_by('date')\
                                .annotate(total_profit= Sum(measure_dict[measure]))\
                                .values_list()
    agg_name = f'total_{measure_dict[measure]}'
    my_array = np.core.records.fromrecords(my_filter, 
                                    names=[f.name for f in DailyData._meta.fields]\
                                     + ['year', 'week', 'month', 'day'] + [agg_name])
    #print(my_array[0])
    #print(my_array[['day','week','month','year']])
    my_dates = [x.date() for x in my_array['date']]
    my_days = [list(calendar.day_name)[y-2] for y in my_array['day']]
    my_months = [list(calendar.month_name)[z] for z in my_array['month']]
    my_weeks = [int(a) for a in my_array['week']]
    ts_dict =  {'daily' : my_dates, 'by weekday': my_days, 
                        'by week': my_weeks, 'by month' : my_months}
    my_choice = my_array[agg_name]
    if cumulative == 'distinct':
        my_plot = go.Figure(data=[go.Bar(x=ts_dict[my_ts], y=my_choice)])
    else:
        my_plot = go.Figure(data=[go.Histogram(x=ts_dict[my_ts], 
                                    y=my_choice, cumulative_enabled=True)])
    my_plot.update_layout(
    autosize=False,
    width=800,
    height=493,
    legend_orientation="h",
    margin_t=25,
    margin_b=25,
    margin_r=25,
    margin_l=50,
    #legend=dict(x=0, y=-0.4),
    yaxis=go.layout.YAxis(
        titlefont=dict(size=15),
        tickformat=tick_dict[measure]
        )
    )
    #return py.plot(my_plot, output_type ='div')
    return my_plot.to_html()