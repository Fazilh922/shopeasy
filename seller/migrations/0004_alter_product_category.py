# Generated by Django 4.2.7 on 2024-01-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(choices=[('dresses', 'dresses'), ('watches', 'watches'), ('phones', 'laptops')], db_column='category', null=True),
        ),
    ]
