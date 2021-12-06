from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class FinanceCourse(models.Model):
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    name = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField()
    file = models.FileField()

    
class BasePageInfo(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField()
            
