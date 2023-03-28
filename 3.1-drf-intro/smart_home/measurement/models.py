from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):

    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')

class Measurement(models.Model):

    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчика')
    temp = models.FloatField(verbose_name='Температура')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    image = models.ImageField(upload_to='users/%Y/%m/%d/', null=True, blank=True, max_length=255)


