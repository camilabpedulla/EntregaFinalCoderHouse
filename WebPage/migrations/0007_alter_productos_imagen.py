# Generated by Django 4.0.6 on 2022-09-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0006_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]