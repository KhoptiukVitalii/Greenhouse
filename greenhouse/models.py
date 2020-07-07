from django.db import models
import json


class AtmosphericPressure(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Тиск"
        verbose_name_plural = "Тиск"


class Temperature(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Температура"
        verbose_name_plural = "Температура"


class Humidity(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Вологість"
        verbose_name_plural = "Вологість"


class SoilTemperature(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Температура грунту"
        verbose_name_plural = "Температура грунту"


class SoilMoisture(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Вологість грунту"
        verbose_name_plural = "Вологість грунту"


class Light(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Освітленість"
        verbose_name_plural = "Освітленість"


class OutsideTemperature(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Температура зовні"
        verbose_name_plural = "Температура зовні"


class HumidityOutside(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Вологість зовні"
        verbose_name_plural = "Вологість зовні"


class ComfortIndicator(models.Model):
    value_date = models.DateTimeField('дата')
    value = models.CharField("значення", max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Показник комфорту"
        verbose_name_plural = "Показник комфорту"
