from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)  
    text = models.TextField()
    #tags = models.ForeginKey()
    #score = models.IntegerField()

    def __str__(self):
        return self.user.username
