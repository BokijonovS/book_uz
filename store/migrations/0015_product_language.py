# Generated by Django 5.0.6 on 2024-07-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_product_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='language',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
