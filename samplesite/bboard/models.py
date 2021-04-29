from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Содержание')
    price = models.FloatField(null=True, blank=True,verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published', 'title', 'rubric']

        def __str__(self):
            return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name
