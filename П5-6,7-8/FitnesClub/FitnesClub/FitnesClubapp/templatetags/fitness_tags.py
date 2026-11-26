from django import template
from django.db.models import Count
from ..models import Client, Exercise, Trainer

register = template.Library()

# считает клиентов
@register.simple_tag
def total_clients():
    return Client.objects.count()

# выводит тренеров
@register.inclusion_tag('tags/trainers_list.html')
def show_trainers():
    trainers = Trainer.objects.all()[:3]
    return {'trainers': trainers}

# номер телефона красиво
@register.filter
def format_phone(value):
    try:
        val = str(value)
        return f"+{val[1:4]} {val[4:7]} {val[7:9]} {val[9:]}"
    except:
        return value