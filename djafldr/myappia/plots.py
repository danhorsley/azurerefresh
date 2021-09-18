from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.offline as py
from .models import DailyData
from django.db.models import Count, Sum, Max, Min
import numpy as np

def dmy(eff):
    return f'{eff.year}-{eff.month:02d}-{eff.day:02d}'

def sales_over_time_chart(measure, timeperiod, title1):

    time_max = DailyData.objects.values().aggregate(Max('date'))['date__max']
    time_min = DailyData.objects.values().aggregate(Min('date'))['date__min']

    time_dict = {'all_time' : time_max-time_min, 
                '7d' : timedelta(days = 50), '30d' : timedelta(days = 30),
                '90d': timedelta(days = 90), '180d': timedelta(days = 180)}
    measure_dict = {'quantity' : 'quantity', 'net profit' : 'net_profit'}
    tick_dict = {'quantity' : ".2", "net profit" : "d"}
    #print(title1)
    
    my_filter = DailyData.objects.filter(itemname__contains = title1,
                                date__range=[dmy(time_max-time_dict[timeperiod]), dmy(time_max)])\
                                .values('date').order_by('date')\
                                .annotate(total_profit= Sum(measure_dict[measure]))\
                                .values_list()
    agg_name = f'total_{measure_dict[measure]}'
    my_array = np.core.records.fromrecords(my_filter, 
                                    names=[f.name for f in DailyData._meta.fields]\
                                    +[agg_name])
    my_dates = [x.date() for x in my_array['date']]
    my_plot = go.Figure(data=[go.Bar(x=my_dates, y=my_array[agg_name])],
                        layout_title_text=f"{measure} of {title1[:20]} over time"
                        )
    my_plot.update_layout(
    autosize=False,
    width=1000,
    height=618,
    legend_orientation="h",
    #legend=dict(x=0, y=-0.4),
    yaxis=go.layout.YAxis(
        titlefont=dict(size=15),
        tickformat=tick_dict[measure]
        )
    )
    return py.plot(my_plot, output_type ='div')