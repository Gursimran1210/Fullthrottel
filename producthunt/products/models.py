from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    url = models.TextField()
    icon = models.ImageField(upload_to='images/')
    votes = models.IntegerField(default=1)
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)

    def short(self):
        return self.body[:80]

    def __str__(self):
        return self.title
