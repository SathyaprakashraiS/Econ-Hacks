# Generated by Django 3.1.3 on 2021-10-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_auto_20211011_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agroproduct',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]