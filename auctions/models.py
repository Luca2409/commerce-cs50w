from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"{self.id}: {self.first_name} \n {self.last_name}"


class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=64)
    image = models.URLField()
    starting_bid= models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.title} \n {self.description} \n {self.image} \n {self.starting_bid} \n {self.category} "

class Bids(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    bid_height = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.name} \n {self.bid_height}"


class Comments(models.Model):
    title = models.CharField(max_length=64)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.id}: {self.title} \n {self.comment}"
    
