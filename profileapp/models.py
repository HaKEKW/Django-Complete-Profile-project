from django.db import models

from django.contrib.auth.models import User

from .logic import calculate_column_averages


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default=0, max_length=200, null=True)
    profile_img = models.ImageField(default='media/test_image.jpg', upload_to='media', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


class PredictedModel(models.Model):
    averages = calculate_column_averages('train.csv')
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
    P1 = models.FloatField(default=averages['P1'])
    P2 = models.FloatField(default=averages['P2'])
    P3 = models.FloatField(default=averages['P3'])
    P4 = models.FloatField(default=averages['P4'])
    P5 = models.FloatField(default=averages['P5'])
    P6 = models.FloatField(default=averages['P6'])
    P7 = models.FloatField(default=averages['P7'])
    P8 = models.FloatField(default=averages['P8'])
    P9 = models.FloatField(default=averages['P9'])
    P10 = models.FloatField(default=averages['P10'])
    P11 = models.FloatField(default=averages['P11'])
    P12 = models.FloatField(default=averages['P12'])
    P13 = models.FloatField(default=averages['P13'])
    P14 = models.FloatField(default=averages['P14'])
    P15 = models.FloatField(default=averages['P15'])
    P16 = models.FloatField(default=averages['P16'])
    P17 = models.FloatField(default=averages['P17'])
    P18 = models.FloatField(default=averages['P18'])
    P19 = models.FloatField(default=averages['P19'])
    P20 = models.FloatField(default=averages['P20'])
    P21 = models.FloatField(default=averages['P21'])
    P22 = models.FloatField(default=averages['P22'])
    P23 = models.FloatField(default=averages['P23'])
    P24 = models.FloatField(default=averages['P24'])
    P25 = models.FloatField(default=averages['P25'])
    P26 = models.FloatField(default=averages['P26'])
    P27 = models.FloatField(default=averages['P27'])
    P28 = models.FloatField(default=averages['P28'])
    P29 = models.FloatField(default=averages['P29'])
    P30 = models.FloatField(default=averages['P30'])
    P31 = models.FloatField(default=averages['P31'])
    P32 = models.FloatField(default=averages['P32'])
    P33 = models.FloatField(default=averages['P33'])
    P34 = models.FloatField(default=averages['P34'])
    P35 = models.FloatField(default=averages['P35'])
    P36 = models.FloatField(default=averages['P36'])
    P37 = models.FloatField(default=averages['P37'])
    results = models.TextField(max_length=200, default='123', null=True)
