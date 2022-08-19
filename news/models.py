from django.db import models


# Create your models here.
#
#
#
#
#
#
#
#
#
#
#

class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)  ## заголовок новости
    content = models.TextField('Описание', blank=True)  ## текст новости
    created_att = models.DateTimeField("Дата создания", auto_now_add=True)  ## дата создания новости
    update_att = models.DateField("Дата обновления", auto_now=True)  ## дата обновления новости
    photo = models.ImageField("Миниатюра", upload_to='images/news/%Y/%m/%d/')  ## фотография новости
    is_published = models.BooleanField("Опубликовано", default=True)  ## опубликована запись или нет
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_att']


class Category(models.Model):
    title = models.CharField('Название категории', max_length=140, db_index=True)
    content = models.CharField('Описание категории', max_length=140)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
