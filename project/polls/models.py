from django.db import models


class Statement(models.Model):
    name = models.TextField(verbose_name='название заявления')

    class Meta:
        verbose_name = 'заявление'
        verbose_name_plural = 'заявления'


class Autor(models.Model):
    name = models.TextField(verbose_name='имя автора')
    statement = models.ForeignKey('Statement', verbose_name='заявление')

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'