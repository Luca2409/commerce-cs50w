from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(WinningHistory)
# Register your models here.
