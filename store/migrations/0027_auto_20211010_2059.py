# Generated by Django 3.1.3 on 2021-10-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20211010_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agroproduct',
            name='image',
            field=models.ImageField(default='images/tst2.png', upload_to='images'),
        ),
    ]
