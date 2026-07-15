from django.db import models 

class Sign(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password1=models.CharField( max_length=50)
    password2=models.CharField(max_length=50)



class Report(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    report_type=models.CharField(max_length=50)
    des=models.CharField(max_length=500)
    

class Help(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    topic=models.CharField(max_length=50)
    message=models.CharField(max_length=1000)
    
    
class Product(models.Model):
    porduct_name=models.CharField(max_length=100)
    
class Adminporduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    img=models.ImageField(null=True,upload_to='')
    dec=models.CharField(max_length=200)
    price=models.IntegerField()
    
class Userpordect(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    img=models.ImageField(null=True,upload_to='')
    dec=models.CharField(max_length=200)
    price=models.IntegerField()
    
