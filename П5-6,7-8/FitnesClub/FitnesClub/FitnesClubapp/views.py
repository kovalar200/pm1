from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Client, Trainer, Exercise, RegistrForExercise

class ClientListView(ListView):
    model = Client
    template_name = 'app.html'
    context_object_name = 'clients'
    paginate_by = 10 # лимит
    def get_queryset(self):
        # поиск по фио
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(full_name__icontains=q)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context
# Карточка тренера + его занятия
class TrainerDetailView(DetailView):
    model = Trainer
    template_name = 'trainer_detail.html'
    context_object_name = 'trainer'
    def get_queryset(self):
        # специализация и занятия
        return super().get_queryset().select_related('specialization_ID').prefetch_related('exercise_set')
class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_form.html'
    fields = ['full_name', 'phone', 'email', 'birth_date']
    success_url = reverse_lazy('client_list')