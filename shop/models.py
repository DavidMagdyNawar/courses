from django.utils import timezone

from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length= 255 )
    created_at = models.DateTimeField(default=timezone.now)


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField
    students_quantity = models.IntegerField()
    reviews_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

