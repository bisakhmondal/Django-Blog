from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    contents=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now) #remind donot pou now()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    #redirect after post is created
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk}) # reverse return url string
    