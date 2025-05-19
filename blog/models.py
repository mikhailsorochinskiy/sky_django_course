from django.db import models

# Create your models here.

class BlogReview(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='photo', blank=True, null=True, verbose_name="Превью", help_text='Загрузите изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_active = models.BooleanField(verbose_name='признак публикации')
    # see_counter = models.IntegerField(,verbose_name='количество просмотров')
    see_counter = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
