from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья Article'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег Tags'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class ArticleTags(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name='Тег')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Связи ArticleTags'
        verbose_name_plural = 'Тег - Статья'
        ordering = ['-is_main']
