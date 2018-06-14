from django.db import models
import datetime


class Customer(models.Model):
    fname = models.CharField('first name', max_length=50)
    lname = models.CharField('last name', max_length=50)
    dob = models.DateField('date of birth', blank=True, null=True)
    phone = models.CharField('phone number', max_length=11, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (self.fname + ' ' + self.lname)

    def birthday_this_month(self):
        return self.dob.month == datetime.datetime.now().month


class Product(models.Model):
    product = models.CharField(max_length=50)
    retail_cost = models.FloatField('price')
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_date = models.DateField()
    tax_rate = models.FloatField()
    discount_percentage = models.FloatField()
    gift_certificate = models.FloatField()
    received = models.BooleanField()
    paid = models.BooleanField()


class Order_Products(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
