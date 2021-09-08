from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Контент')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Редактировано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Загружено?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Comment(models.Model):
    article = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=300)
