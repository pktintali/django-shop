# Generated by Django 4.0a1 on 2021-09-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_product_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-'),
            preserve_default=False,
        ),
    ]
