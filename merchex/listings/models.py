from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Genre(models.TextChoices):
    HIP_HOP = 'HH'
    SYNTH_POP = 'SP'
    ALTERNATIVE_ROCK = 'AR'


class Type(models.TextChoices):
    Records = 'Rec'
    Clothing = 'Clo'
    Posters = 'Pos'
    Miscellaneous = 'Mis'


class Band(models.Model):
    name = models.CharField(max_length=100)

    biography = models.CharField(max_length=1000, null=True, blank=True)
    year_formed = models.IntegerField(null=True, blank=True,
                                      validators=[MinValueValidator(
                                          1900), MaxValueValidator(2021)]
                                      )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    genre = models.CharField(choices=Genre.choices,
                             null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name


class Listing(models.Model):
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    description = models.CharField(default='', max_length=100)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(null=True, blank=True,
                               validators=[MinValueValidator(
                                   1900), MaxValueValidator(2021)]
                               )
    type = models.CharField(choices=Type.choices,
                            null=True, blank=True, max_length=50)

    def __str__(self):
        return self.title
