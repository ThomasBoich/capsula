from django import template
from news.models import *

register = template.Library()


# ПОЛУЧЕНИЕ СПИСКА КАТЕГОРИЙ В ТЭГ СПОСОБ 1
#
# @register.simple_tag(name='get_list_categories')
# def get_categories():
#     return Category.objects.all()
#
# {% get_list_categories as categories %}
# {% for item in categories %}
# <a href="{% url 'category' item.pk %}">{{ item.title }}</a>
# {% endfor %}

# ПОЛУЧЕНИЕ СПИСКА КАТЕГОРИЙ В ТЭГ СПОСОБ 2
@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
