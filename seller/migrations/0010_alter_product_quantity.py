# Generated by Django 4.2.7 on 2024-01-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0009_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(db_column='quantity', null=True),
        ),
    ]
