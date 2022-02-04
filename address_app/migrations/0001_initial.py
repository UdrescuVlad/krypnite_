# Generated by Django 3.2.12 on 2022-02-03 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing_app', '0002_alter_billingprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_address', models.CharField(max_length=120)),
                ('secondary_address', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(default='Romania', max_length=120)),
                ('state_province', models.CharField(max_length=120)),
                ('postal_code', models.CharField(max_length=120)),
                ('billing_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing_app.billingprofile')),
            ],
        ),
    ]