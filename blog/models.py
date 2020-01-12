from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Comments(models.Model):
    author=models.ForeignKey(User,on_delete=models.PROTECT) # ensuring deleting user dont delete comments on other's post
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    post=models.ForeignKey('Post',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.author} cmnt'
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.post.id})

class Post(models.Model):
    title=models.CharField(max_length=100)
    contents=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now) #remind donot pou now()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # comments=models.OneToOneField(Comments,on_delete=models.PROTECT,null=True)# deleting post delete comment

    def __str__(self):
        return self.title
    #redirect after post is created
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk}) # reverse return url string
    
Comments.parent_post=models.OneToOneField(Post,on_delete=models.CASCADE)