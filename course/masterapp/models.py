from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class FinanceCourseLable(models.Model):
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class FinanceCourse(models.Model):
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    name = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(blank="True")
    file = models.FileField(blank="True")

    def __str__(self):
        return self.name

    
class BasePageInfo(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField()
            
