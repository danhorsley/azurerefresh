from myappia.models import *
import numpy as np
import plotly.graph_objects as go
my_filter = DailyData.objects.all().filter(itemname__contains = 'Richer').values_list()
my_array = np.core.records.fromrecords(my_filter, names=[f.name for f in DailyData._meta.fields])
my_plot = go.Figure(data=[go.Bar(x=my_array['date'], y=my_array['net_profit'])])
my_plot.show()