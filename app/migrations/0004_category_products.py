# Generated by Django 4.2.1 on 2023-05-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_attribute_category_order_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='categories', to='app.product'),
        ),
    ]
