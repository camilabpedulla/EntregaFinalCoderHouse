# Generated by Django 4.1 on 2022-09-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajes', '0006_alter_mensajes_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='fecha',
            field=models.DateField(blank=True, db_column='fecha', default='%Y-%m-%d', null=True),
        ),
    ]
