from django.db import models

class Titles(models.Model):
    title = models.CharField("Название тайтла",max_length=150)
    rate = models.IntegerField("Оценка",default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тайтл"
        verbose_name_plural = "Тайтлы"