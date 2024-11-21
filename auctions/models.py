from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"{self.id}: {self.first_name} \n {self.last_name}"
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user" )
    bid = models.IntegerField()

class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=64)
    image = models.URLField()
    starting_bid = models.IntegerField()
    current_bid = models.ManyToManyField(Bid, related_name="current_bid") 
    
    def __str__(self):
        return f"{self.id}: {self.title} \n {self.description} \n {self.image} \n {self.starting_bid} \n {self.category} "

class Comments(models.Model):
    title = models.CharField(max_length=64)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.id}: {self.title} \n {self.comment}"
    
class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    listing_id = models.ManyToManyField(Listings, related_name="listing_id")

    def __str__(self):
        return f"{self.id}: {self.user_id} \n {self.listing_id}"