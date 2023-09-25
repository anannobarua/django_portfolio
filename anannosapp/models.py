from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_file_type(value):
    # Define a function to validate the file type
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mov', 'avi']
    extension = value.name.split('.')[-1]
    if extension.lower() not in valid_extensions:
        raise ValidationError(_('File type is not supported.'))
    
class Portfolio(models.Model):
    project_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, max_length=10000)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_type],null=True)
    github_link = models.URLField(blank=True, null=True)
    #for showing in the admin panel
    def __str__(self):
        return f"{self.title}"


# Create your models here.

class About(models.Model):
    about_id=models.AutoField(primary_key=True)
    description = models.TextField(null=True, max_length=10000)
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    published_date = models.DateField(auto_now_add=True,null=True)
    file=models.FileField(null=True,upload_to="files/")
    
    
    def __str__(self):
        return f"{self.published_date}"




    

# class Vlog(models.Model):
    

class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(null=True, max_length=100)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    description = models.TextField(null=True, max_length=100)
    
     #for showing in the admin panel
    def __str__(self):
        return f"{self.name} -- {self.email}"