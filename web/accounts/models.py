from django.db import models

# Create your models here.
class USer (models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    username= models.CharField(max_length=30)
    email= models.EmailField(max_length=50)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

    def _str_(self):
    	return self.email