from django.db import models

# Create your models here.
class Seller(models.Model):
    name=models.TextField(db_column='name',null=True)
    email=models.TextField(db_column='email',null=True)
    number=models.TextField(db_column='number',null=True)
    password=models.TextField(db_column='password',null=True)

    class Meta:
        db_table='seller_signin'
class Category(models.Model):
    name=models.TextField(max_length=100,null=True)
    image=models.ImageField(null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    product=models.TextField(db_column='product',null=True)
    description=models.TextField(db_column='description',null=True)
    image=models.ImageField(upload_to='products',db_column='image',null=True)
    stock=models.TextField(db_column='stock',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(db_column='quantity',null=True)
    price=models.PositiveIntegerField(db_column='price',null=True)
    def __str__(self):
        return self.product


    



