from django.db import models

# Create your models here.
# The Category class is a model that has a title field that is a CharField with a max length of 255
# characters
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

# A Book has a title, author, isbn, pages, price, quantity, description, status, and date_created
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, default='John Doe')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

# The Grocery class is a model that has a product_tag, name, category, price, quantity, imageurl,
# status, and date_created
class Grocery(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='grocery', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    imageurl = models.URLField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name