from django.db import models

class Cafe(models.Model):
    title = models.CharField('Назва', max_length=50)
    address = models.CharField('Адреса', max_length=100)
    text = models.TextField('Опис')
    published = models.IntegerField('Відкрито заклад', default='2022')
    price = models.IntegerField('Середній чек, ₴')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Meta:
    verbose_name = 'Cafe'
    verbose_name_plural = 'Cafes'