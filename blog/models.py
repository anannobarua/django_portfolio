from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_file_type(value):
    # Define a function to validate the file type
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mov', 'avi']
    extension = value.name.split('.')[-1]
    if extension.lower() not in valid_extensions:
        raise ValidationError(_('File type is not supported.'))
    
class Blog(models.Model):
    p_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, max_length=10000)
    url=models.URLField(null=True,max_length=20)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_type],null=True)
    # github_link = models.URLField(blank=True, null=True)
    
    #for showing in the admin panel
    def __str__(self):
        return f"{self.title}"
