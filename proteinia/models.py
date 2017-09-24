from django.db import models

# Create your models here.

''' Product information for sale '''
class Product(models.Model):
    productid = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    desc = models.TextField(null=True)
    comment = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    isavailable = models.BooleanField()

    class Meta:
        ordering = ('-productid',)
    
    def __unicode__(self):
        return self.productid + ": "

class Customer(models.Model):
    customerId = models.PositiveIntegerField(primary_key=True)
    personId = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)
    name = models.TextField()
    desc = models.TextField()
    address = models.TextField()
    homePhone = models.TextField()
    cellPhone = models.TextField()

class TransactionRecord(models.Model):
    recordIdse = models.PositiveIntegerField(primary_key=True)
    buyDate = models.DateTimeField()
    customerId = models.PositiveIntegerField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
