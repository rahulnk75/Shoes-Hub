# Generated by Django 5.1.2 on 2024-10-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoes_App', '0004_rename_product_category_product_db_shoes_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_db',
            name='Size',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
