# Generated by Django 3.2.21 on 2023-12-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20231224_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avater',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]