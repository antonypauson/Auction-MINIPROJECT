# Generated by Django 5.0.3 on 2024-05-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_auctionlisting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='end_time',
            field=models.DateTimeField(blank=True, help_text='Set the end time for the auction.', null=True),
        ),
    ]