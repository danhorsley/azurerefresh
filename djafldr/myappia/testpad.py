from myappia.models import *
import numpy as np
import plotly.graph_objects as go
#my_filter = DailyData.objects.all().filter(itemname__contains = 'Richer').values_list()
my_filter = DailyData.objects.values('date').order_by('date').annotate(totalp = Sum('net_profit')).values_list()
my_array = np.core.records.fromrecords(my_filter, names=[f.name for f in DailyData._meta.fields])
my_date = [x.date() for x in my_array['date']]
my_plot = go.Figure(data=[go.Bar(x=, y=my_array['net_profit'])])
my_plot.show()

<embed type="image/svg+xml" src= {{html_plot|safe}}>
        </embed>