# Generated by Django 3.1.3 on 2021-10-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_agroproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_farmer',
            field=models.BooleanField(default=False),
        ),
    ]
