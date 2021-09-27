from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('subject/<str:pk>',views.subject, name='subject'),
    path('topic/<str:pk>',views.topic, name='topic'),
    path('subtopic/<str:pk>',views.subtopic, name='subtopic'),
    path('subjectList', views.subjectList, name='subjectList'),
]