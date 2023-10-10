from django.db import models


class VWCar(models.Model):
    manufacturer = models.CharField(max_length=250, verbose_name='Brand', default='VAG', editable=False)
    diesel_engine = models.ForeignKey('DieselEngine', on_delete=models.CASCADE)
    date_to_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.manufacturer


class ModelOfCar(models.Model):
    CHOISE_MODEL = [
        ('Golf', 'golf'),
        ('Scirocco', 'scirocco'),
    ]
    manufacturer = models.ForeignKey('VWCar', on_delete=models.CASCADE)
    model_of_car = models.CharField(max_length=250, choices=CHOISE_MODEL)
    image = models.ImageField(upload_to='storage', verbose_name='выбрать файл для загрузки', blank=True)
    date_to_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model_of_car


class DieselEngine(models.Model):
    CHOISE_FUEL_SYSTEM = [
        ('TDI PD', 'PumpDuse system with turbocharger'),
        ('Diesel PD', 'PumpDuse system without turbocharger'),
        ('TDI CR', 'Common Rail system with turbocharger'),
    ]
    type_of_fuel_sytem = models.CharField(max_length=250, verbose_name='Type of fuel system', choices=CHOISE_FUEL_SYSTEM)
    image = models.ImageField(upload_to='storage', verbose_name='выбрать файл для загрузки', blank=True)
    date_to_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type_of_fuel_sytem


