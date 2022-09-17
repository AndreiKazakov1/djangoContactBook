from django.db import models


class Name(models.Model):
    user_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')


class Contact(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='images/')
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postcode = models.IntegerField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
