from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name='Model phone')
    price = models.CharField(max_length=60, verbose_name='Price')
    image = models.FileField(verbose_name='image')
    release_date = models.DateField(verbose_name='Date')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')