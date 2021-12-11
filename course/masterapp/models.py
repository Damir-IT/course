from django.db import models

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
    day_number = models.CharField(max_length=256, null=True, verbose_name="день курса")

    title_exercise_extra = models.CharField(max_length=256, verbose_name='Екста Задание: название', blank="True")
    exercise_extra = models.TextField(blank="True", null=True, verbose_name='задачи "экстразадания"')

    title_exercise_1 = models.CharField(max_length=256, verbose_name='Первое задание: название', blank="True")
    exercise_1 = models.TextField(blank="True", null=True, verbose_name='Первое задание: задачи')

    title_exercise_2 = models.CharField(max_length=256, verbose_name='Второе задание: название', blank="True")
    exercise_2 = models.TextField(blank="True", null=True, verbose_name='Второе задание: задачи')

    title_image = models.CharField(max_length=256, verbose_name='Название картинки', blank="True")
    description_image = models.TextField(verbose_name='Описание картинки', blank="True")
    image = models.ImageField(upload_to='masterapp/image', blank="True", null=True, verbose_name='картинка')

    title_check_list = models.CharField(max_length=256, verbose_name='название чек-листа', blank="True")
    description_check_list = models.TextField(verbose_name='описание чек листа', blank="True")
    check_list = models.FileField(upload_to='masterapp/check_list', blank="True", null=True, verbose_name='чек лист')

    title_audio_file = models.CharField(max_length=256, verbose_name='Название медитации', blank="True")
    description_audio_file = models.TextField(verbose_name='Описание медитации', blank="True")
    audio_file = models.FileField(upload_to='masterapp/audio_file', blank="True", null=True, verbose_name='медитация')

    def __str__(self):
        return self.day_number

    class Meta:
        verbose_name = "Модель курса"
        verbose_name_plural = "Модели курса"

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
class BasePageInfo(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField()
            
