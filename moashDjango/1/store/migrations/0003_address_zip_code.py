# Generated by Django 4.2.7 on 2023-12-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default='5010', max_length=255),
            preserve_default=False,
        ),
    ]
