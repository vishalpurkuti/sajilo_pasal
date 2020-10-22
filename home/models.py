from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=20)
    cat_desc=models.TextField()

    def __str__(self):
        return self.cat_name
    

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    product_cat=models.name = models.ForeignKey('Category',  on_delete=models.CASCADE)
    image1=models.ImageField(upload_to='static/products')
    description=models.TextField()

    def __str__(self):
        return self.name