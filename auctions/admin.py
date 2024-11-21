from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Comments)
admin.site.register(Bid)
admin.site.register(Watchlist)
# Register your models here.
