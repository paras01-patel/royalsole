from django.db import models 

class Sign(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password1=models.CharField( max_length=50)
    password2=models.CharField(max_length=50)

