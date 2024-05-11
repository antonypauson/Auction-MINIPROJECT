# Generated by Django 5.0.3 on 2024-05-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='image_url',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='uploads/'),
        ),
    ]
