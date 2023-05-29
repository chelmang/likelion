from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100) #블로그 제목
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Post(models.Model): # pk값 지정 안 하면 Django가 알아서 판단하고 생성
    title = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content



