from django import template  

from basic.models import Subject  

register = template.Library()  

@register.inclusion_tag("subjectList.html")
def show_subjects():
    subjects = Subject.objects.all()
    return {'subjects':subjects} 
