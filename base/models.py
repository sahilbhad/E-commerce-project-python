from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=180)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    image=models.ImageField(default='defult.png')
    t=models.BooleanField(default=False)
    o=models.BooleanField(default=False)


class cart(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=180)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    q=models.IntegerField(default=0)
    total_p=models.IntegerField(default=0)
    image=models.ImageField(default='defult.png')
    host=models.ForeignKey(User,on_delete=models.CASCADE)

 
   
  

sname=(
    ('gujrat','gujrat'),
    ('haryana','haryana'),
)

class checkout(models.Model):
    fullname=models.CharField(max_length=50)
    address=models.TextField()
    phonenumber=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    state=models.CharField(choices=sname,max_length=100)
    zipcode=models.CharField(max_length=6)
    card_num=models.CharField(max_length=16)
    e_date=models.CharField(max_length=4)
    cvv=models.CharField(max_length=3)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
   


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=180)
    price=models.IntegerField(default=0)
    q=models.IntegerField(default=0)
    total_p=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)


