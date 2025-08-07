from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']  # Sorts alphabetically by default

    def __str__(self):
        return self.name  # This will display the category name



User = get_user_model()

class TODOO(models.Model):
    srno = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    reminder = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.category.name if self.category else 'No Category'}"
