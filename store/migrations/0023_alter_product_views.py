# Generated by Django 5.0.6 on 2024-07-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_product_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
