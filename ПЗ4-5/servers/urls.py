from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logs/', views.logs_view, name='logs'),
    path('create/', views.create_query_view, name='create'),
]