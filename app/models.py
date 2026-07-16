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
    


class Merchant_signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class MerchantVerification(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER)
    dob = models.DateField()
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    profile = models.ImageField(upload_to='merchant/profile/')
    aadhaar = models.CharField(max_length=12)
    aadhaar_file = models.FileField(upload_to='merchant/aadhaar/')
    pan = models.CharField(max_length=10)
    pan_file = models.FileField(upload_to='merchant/pan/')
    account_holder = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=11)
    passbook = models.FileField(upload_to='merchant/passbook/')
    created_at = models.DateTimeField(auto_now_add=True)