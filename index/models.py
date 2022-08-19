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
