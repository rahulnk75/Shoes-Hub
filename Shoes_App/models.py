from django.db import models

# Create your models here.
class Category_Db(models.Model):
    Shoes_Category=models.CharField(max_length=200,null=True,blank=True)
    Shoes_Brand=models.CharField(max_length=200,null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)
    Shoes_Images=models.ImageField(upload_to='Category_images',null=True,blank=True) 

class Product_Db(models.Model):
    Shoes_Category=models.CharField(max_length=200,blank=True,null=True)
    Shoes_Brand=models.CharField(max_length=200,blank=True,null=True)
    Product_Name=models.CharField(max_length=200,blank=True,null=True)
    Quantity=models.IntegerField(blank=True,null=True)
    Country_of_origin=models.CharField(max_length=200,blank=True,null=True)
    Manufactured_By=models.CharField(max_length=200,blank=True,null=True)
    Description=models.TextField(max_length=200,blank=True,null=True)
    MRP=models.IntegerField(blank=True,null=True)
    Size=models.CharField(max_length=200,blank=True,null=True)
    Product_Image_1=models.ImageField(upload_to='Product_Images',blank=True,null=True)
    Product_Image_2=models.ImageField(upload_to='Product_Images',blank=True,null=True)
    Product_Image_3=models.ImageField(upload_to='Product_Images',blank=True,null=True)
    Product_Image_4=models.ImageField(upload_to='Product_Images',blank=True,null=True)
    Product_Image_5=models.ImageField(upload_to='Product_Images',blank=True,null=True)

