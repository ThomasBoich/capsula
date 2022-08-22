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

class Index(models.Model):
    title = models.CharField(max_length=200)  ## заголовок новости
    content = models.TextField(blank=True)  ## текст новости
    created_att = models.DateTimeField(auto_now_add=True)  ## дата создания новости
    update_att = models.DateField(auto_now=True)  ## дата обновления новости
    photo = models.ImageField(upload_to='images/news/%Y/%m/%d/')  ## фотография новости
    is_published = models.BooleanField(default=True)  ## опубликована запись или нет

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
        ordering = ['created_att']

class Contacts(models.Model):
    title = models.CharField(max_length=200)  ## заголовок новости
    content = models.TextField(max_length=2000, blank=True)  ## текст новости
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=200)
    # website = models.CharField(max_length=200)
    # #timework = models.CharField(max_length=200)
    # compmany = models.CharField(max_length=200)
    # ogrn = models.CharField(max_length=200)
    # inn = models.CharField(max_length=200)
    # website = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        ##ordering = ['created_att']