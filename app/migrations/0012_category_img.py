# Generated by Django 4.2 on 2023-06-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_categoryy'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(null=True, upload_to='priview'),
        ),
    ]
