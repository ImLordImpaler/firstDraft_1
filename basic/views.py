from django.shortcuts import render
from .models import *

def index(request):
    subjects = Subject.objects.all() 
    context = { 
        'subjects':subjects
    }
    return render(request , 'index2.html', context)


def subject(request,pk): 
    subject = Subject.objects.get(id=pk)
    
    topics = Topic.objects.filter(subject__id=subject.id)
    
    context = { 
        'subject':subject,
        'topics':topics

    }
    return render(request , 'subject.html', context)

def topic(request,pk):
    topic = Topic.objects.get(id=pk) 
    subtopics = SubTopic.objects.filter(topic__name= topic.name)

    
    context = { 
        'topic':topic,
        'subtopics':subtopics
    }
    return render(request , 'topic.html', context)

def subtopic(request,pk):
    subtopic = SubTopic.objects.get(id=pk)
    subsubtopics = SubSubTopic.objects.filter(subtopic__id= subtopic.id)
    params = {
        'subtopic':subtopic,
        'subsubtopics':subsubtopics
    }

    return render(request , 'subtopic.html',params)

def subjectList(request):
    subjects = Subject.objects.all()
    context = {
        'subjects':subjects
    }
    return render(request , 'subjectsPage.html', context)