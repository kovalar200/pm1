from django.urls import path
from .views import ClientListView, TrainerDetailView, ClientCreateView

app_name = 'fitness'

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('trainers/<int:pk>/', TrainerDetailView.as_view(), name='trainer_detail'),
]