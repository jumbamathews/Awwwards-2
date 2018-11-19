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


class Project(models.Model):
    project_title = models.CharField(max_length=40)
    project_description = HTMLField()
    landing_page = models.ImageField(upload_to='landing_pages')
    live_site = URLOrRelativeURLField()
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)


    def __str__(self):
        return self.project_title
