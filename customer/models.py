from django.db import models
from seller.models import Product

# Create your models here.
class Customer(models.Model):
    name=models.TextField(db_column='name',null=True)
    email=models.TextField(db_column='email',null=True)
    number=models.TextField(db_column='number',null=True)
    password=models.TextField(db_column='password',null=True)
   

    class Meta:
        db_table='customer_signin'
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)


class Messages(models.Model):
    name=models.TextField(db_column='name',null=True)
    email=models.TextField(db_column='email',null=True)
    number=models.TextField(db_column='number',null=True)
    text=models.TextField(db_column='text',null=True)


