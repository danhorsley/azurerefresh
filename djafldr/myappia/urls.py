from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('answer/', views.answer, name='answer'),
    path('', views.homepage, name='home'),
    path('query2', views.query2, name='query2'),
    path('presets', views.presets, name='presets'),

]
