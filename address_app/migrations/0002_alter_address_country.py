# Generated by Django 3.2.12 on 2022-02-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(choices=[('ro', 'Romania')], default='ro', max_length=120),
        ),
    ]