# Generated by Django 4.0.4 on 2022-12-21 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_rate_vendorrate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VendorRate',
        ),
    ]
