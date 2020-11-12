from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    description=models.CharField(max_length=500)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name
    
    