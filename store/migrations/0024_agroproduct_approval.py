# Generated by Django 3.1.3 on 2021-10-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20211010_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='agroproduct',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
