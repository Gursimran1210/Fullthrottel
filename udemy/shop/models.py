from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50,default="")
    subcatagory = models.CharField(max_length=50,default="")
    #price = models.IntegerField(5005000)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    comment = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.first_name





