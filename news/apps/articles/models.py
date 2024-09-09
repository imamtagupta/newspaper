from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)    
    joined_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"
    

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="static/thumnails/", null=True, blank=True)
    published_dt = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    category = models.ManyToManyField(Category, related_name="articles", blank=True)

    def __str__(self):
        return self.title

    


