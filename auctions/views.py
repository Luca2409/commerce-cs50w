from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.db.models import Max

from .models import *
from .forms import CreateListing, SubmitBid, CommentForm

import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })

def Delete(request, id):
    listing = Listing.objects.get(id=id)
    logger.warning(listing)
    if request.user == listing.added_by:
        listing.closed = True
        listing.save()
        
        bids = Bid.objects.filter(listing=listing)

        max_bid = bids.aggregate(Max("bid"))["bid__max"]

        winner = Bid.objects.filter(listing=listing, bid=max_bid).first()

        if winner:  
            win, created = WinningHistory.objects.get_or_create(user=winner.user)

            win.wins.add(listing)

        return redirect("index")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = CreateListing(request.POST)
        logger.warning(form)
        if form.is_valid():
            data = form.cleaned_data
            logger.warning(data)
            listing = Listing(title=data['title'], description=data['description'], image=data['picture'], category=data['category'], starting_bid=data['bid_height'])
            listing.added_by = user
            listing.save()
            
            return render(request, "auctions/create.html", {
            "form": CreateListing(), 
            "message": "Success."
        })
        else:
            return render(request, "auctions/create.html", {
            "form": CreateListing(),
            "message": "Form is not valid."
        })
    else:
        return render(request, "auctions/create.html", {
            "form": CreateListing()
        })
    

def listings(request, id):
    
    if request.method == "POST":
        logger.warning(id)
        form = SubmitBid(request.POST)
        if form.is_valid():

            data = form.cleaned_data 
            user = User.objects.get(id=request.user.id)
            listing = Listing.objects.get(id=id)
            
            bids = Bid.objects.filter(listing=id).values()
            bid_height = [0]

            for bid in bids: 
                bid_height.append(bid["bid"])

            if data["bid"] <= listing.starting_bid or data["bid"] <= max(bid_height):
                listing = Listing.objects.get(id=id)
                return render(request, "auctions/listings.html", {
                "form": SubmitBid(),
                "listing": listing,
                "comment": CommentForm(),
                "comments": Comment.objects.get(listing=id).values(),
                "user": WinningHistory.objects.get(wins=listing).user,
                "message": "Bid is too low."
            })
            else: 
                listing = Listing.objects.get(id=id)
                bid = Bid(bid=data["bid"])
                bid.user = user
                bid.listing = listing
                bid.save()
                
                listing.starting_bid = data["bid"]
                listing.save()

                return render(request, "auctions/listings.html", {
                    "form": SubmitBid(),
                    "listing": listing,
                    "comment": CommentForm(),
                    "comments": Comment.objects.filter(listing=id).values(),
                    "user": WinningHistory.objects.get(wins=listing).user,
                    "message": "Successfully submitted bid."
                })
            
        return HttpResponse("Form not valid.")
    
    else:

        listing = Listing.objects.get(id=id)

        return render(request, "auctions/listings.html" , {
            "form": SubmitBid(),
            "watchlist": listings,
            "comment": CommentForm(),
            "comments": Comment.objects.filter(listing=id).values(),
            "user": WinningHistory.objects.get(wins=listing).user,
            "listing": listing
        })
            
def WatchlistView(request):
    watchlist = Watchlist.objects.get(user=request.user.id)
    listings = watchlist.listing.all()

    return render(request, "auctions/watchlist.html" , {
        "watchlist": listings,
    })

def AddWatchlist(request, id):
    if request.method == "POST":
        watchlist = Watchlist.objects.get(user=request.user.id)

        listing = Listing.objects.get(id=id)

        watchlist.listing.add(listing)

        return redirect("listings", id=id)
    

def DeleteWatchlist(request, id):
    if request.method == "POST":
        watchlist = Watchlist.objects.get(user=request.user.id)

        listing = Listing.objects.get(id=id)
        watchlist.listing.remove(listing)

        return redirect("listings", id=id)
    

def Categories(request):

    listings = Listing.objects.all().values()
    category = []

    for listing in listings:
        
        category.append(listing["category"])

    category_final = set(category)
    
    return render(request, "auctions/categories.html" , {
        "categories": category_final
    })
    
def CategoryPage(request, category):
    listings = Listing.objects.filter(category=category).values()

    return render(request, "auctions/categorypage.html" , {
        "listings": listings
    })

def CommentView(request, id):
    user = User.objects.get(id=request.user.id)
    listing = Listing.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment(title=data["title"], comment=data["text"])
            comment.listing = listing
            comment.user = user
            comment.save()
        return redirect("listings", id=id)
    return redirect("listings", id=id)
    
def WinHistory(request):

    user = User.objects.get(id=request.user.id)

    listing = WinningHistory.objects.get(user=user)

    history = listing.wins.all()
    
    return render(request, "auctions/winninghistory.html" , {
        "listings": history
    })
    pass
        
    