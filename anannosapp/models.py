from django.db import models


# Create your models here.

class About(models.Model):
    about_id=models.AutoField(primary_key=True)
    description = models.TextField(null=True, max_length=10000)
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    published_date = models.DateField(auto_now_add=True,null=True)
    file=models.FileField(null=True,upload_to="files/")
    def __str__(self):
        return f"{self.published_date}"

class Portfolio(models.Model):
    project_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    video_file = models.FileField(null=True, upload_to='videos/')
    
    #for showing in the admin panel
    def __str__(self):
        return f"{self.title}"
    #for upload one between two 
    def save(self, *args, **kwargs):
        if not self.image and not self.video_file:
            raise ValueError("At least one of Image or Video must be filled.")
        super(Portfolio, self).save(*args, **kwargs)

# class Vlog(models.Model):
    

class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    first_name=models.CharField(null=True, max_length=100)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    description = models.TextField(null=True, max_length=100)
    
     #for showing in the admin panel
    def __str__(self):
        return f"{self.first_name} -- {self.email}"