# Generated by Django 3.1.3 on 2021-10-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_agroproduct_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agroproduct',
            name='image',
            field=models.ImageField(default='images/tst2.jpg', upload_to='images'),
        ),
    ]
