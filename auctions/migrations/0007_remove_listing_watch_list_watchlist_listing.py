# Generated by Django 5.1.3 on 2024-11-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0006_rename_listing_id_bid_listing_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listing",
            name="watch_list",
        ),
        migrations.AddField(
            model_name="watchlist",
            name="listing",
            field=models.ManyToManyField(to="auctions.listing"),
        ),
    ]
