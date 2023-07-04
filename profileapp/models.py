from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default=0, max_length=200, null=True)
    profile_img = models.ImageField(default='media/test_image.jpg', upload_to='media', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


class PredictedModel(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    open_days = models.IntegerField(default=1)
    city_name = models.TextField(default='Minsk', max_length=200)
    TYPES = (
        ('IL', 'IL'),
        ('FC', 'FC'),
    )
    TRUE = (
        (1, 'True'),
        (2, 'False')
    )
    big_cities = models.IntegerField(choices=TRUE)
    type = models.TextField(choices=TYPES, default='IL')
    P1 = models.FloatField(default=0)
    P2 = models.FloatField(default=0)
    P3 = models.FloatField(default=0)
    P4 = models.FloatField(default=0)
    P5 = models.FloatField(default=0)
    P6 = models.FloatField(default=0)
    P7 = models.FloatField(default=0)
    P8 = models.FloatField(default=0)
    P9 = models.FloatField(default=0)
    P10 = models.FloatField(default=0)
    P11 = models.FloatField(default=0)
    P12 = models.FloatField(default=0)
    P13 = models.FloatField(default=0)
    P14 = models.FloatField(default=0)
    P15 = models.FloatField(default=0)
    P16 = models.FloatField(default=0)
    P17 = models.FloatField(default=0)
    P18 = models.FloatField(default=0)
    P19 = models.FloatField(default=0)
    P20 = models.FloatField(default=0)
    P21 = models.FloatField(default=0)
    P22 = models.FloatField(default=0)
    P23 = models.FloatField(default=0)
    P24 = models.FloatField(default=0)
    P25 = models.FloatField(default=0)
    P26 = models.FloatField(default=0)
    P27 = models.FloatField(default=0)
    P28 = models.FloatField(default=0)
    P29 = models.FloatField(default=0)
    P30 = models.FloatField(default=0)
    P31 = models.FloatField(default=0)
    P32 = models.FloatField(default=0)
    P33 = models.FloatField(default=0)
    P34 = models.FloatField(default=0)
    P35 = models.FloatField(default=0)
    P36 = models.FloatField(default=0)
    P37 = models.FloatField(default=0)

    results = models.TextField(max_length=200, default='123')
