
from django.urls import path

import todo.views as views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add'),
    path('list/', views.get_task, name='list'),
]
