# Generated by Django 4.2.2 on 2023-07-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0006_alter_predictedmodel_p2_alter_predictedmodel_p22_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictedmodel',
            name='results',
            field=models.TextField(default='123', max_length=200),
        ),
    ]