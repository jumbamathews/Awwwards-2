from django.db import models
from url_or_relative_url_field.fields import URLOrRelativeURLField
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_photos',null=True,blank=True)
    bio = HTMLField()
    contact=models.CharField(max_length=12)
    linkedIn =  URLOrRelativeURLField()
    projects = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username
