from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image')
    image_alt = models.CharField(max_length=200, null=True)
    website_link = models.URLField(max_length=200, null=True, blank=True)
    repo_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
    