from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    
class Profile(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')


    def __str__(self):
        return f'{self.user_id}'
