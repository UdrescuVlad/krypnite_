# Generated by Django 3.2.9 on 2021-11-16 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krypniteweb', '0004_registrationmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationmodel',
            old_name='username',
            new_name='email',
        ),
    ]
