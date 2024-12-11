# Generated by Django 5.1.2 on 2024-11-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0003_cart_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Place', models.CharField(blank=True, max_length=200, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('Message', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
