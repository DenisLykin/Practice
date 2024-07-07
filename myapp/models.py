from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey('City', on_delete=models.PROTECT)

    class Meta:
        unique_together = (('name', 'city'),)

    def __str__(self):
        return f'{self.name}, {self.city}'

class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    street = models.ForeignKey('Street', on_delete=models.PROTECT)
    house = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.name