from django import template
register = template.Library()

@register.filter(name='get_thread')
def get_thread(threads, category):
    return threads.get(category)