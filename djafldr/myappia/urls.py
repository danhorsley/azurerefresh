from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('answer/', views.answer, name='answer'),
    path('', views.homepage, name='home'),

]
