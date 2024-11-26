# Generated by Django 5.1.3 on 2024-11-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0004_bid_comment_watchlist_listing_watch_list"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listing",
            name="watch_list",
        ),
        migrations.AddField(
            model_name="listing",
            name="watch_list",
            field=models.ManyToManyField(
                blank=True, null=True, to="auctions.watchlist"
            ),
        ),
    ]
