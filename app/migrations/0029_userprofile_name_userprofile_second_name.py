# Generated by Django 4.2.1 on 2023-06-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_remove_userprofile_contact_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Отчевство'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='second_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Отчевство'),
        ),
    ]
