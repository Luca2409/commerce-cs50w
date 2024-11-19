from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthday = models.DateField()

    def __str__(self):
        return f"{self.id}: {self.first_name} \n {self.last_name}"


class Listings():
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    image = models.ImageField()
    starting_bid= models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.title} \n {self.description} \n {self.image} \n {self.starting_bid} "

class Bids():
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    bid_height = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.name} \n {self.bid_height}"


class Comments():
    title = models.CharField(max_length=64)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.id}: {self.title} \n {self.comment}"
    
