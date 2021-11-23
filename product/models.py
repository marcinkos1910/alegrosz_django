from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    image = models.ImageField(upload_to='media', blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    subcategory = models.ForeignKey("Subcategory", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    content = models.TextField(max_length=500)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}."
