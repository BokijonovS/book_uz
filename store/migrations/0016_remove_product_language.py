# Generated by Django 5.0.6 on 2024-07-01 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_product_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='language',
        ),
    ]