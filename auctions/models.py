from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    
class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=64)
    image = models.URLField()
    starting_bid = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
    closed = models.BooleanField(blank=True, null=True)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True)
    bid = models.IntegerField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=64)
    comment = models.CharField(max_length=300)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True)

class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    listing = models.ManyToManyField(Listing, related_name="watchlist_listing")

class WinningHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wins = models.ManyToManyField(Listing)
