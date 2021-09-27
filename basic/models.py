from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=10000)
    opening  = models.TextField() 

    img1 = models.ImageField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=10000)
    desc = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 

    img1 = models.ImageField() 

    def __str__(self): 
        return self.name  

class SubTopic(models.Model):
    name= models.CharField(max_length=10000)
    img1 = models.ImageField()

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):  
        return self.name 


class SubSubTopic(models.Model):
    text = models.TextField()   
    img1 = models.ImageField() 
    subtopic = models.ForeignKey(SubTopic, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return str(self.subtopic.name+ ' ' + self.text)

