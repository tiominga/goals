# Generated by Django 5.0 on 2023-12-15 11:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_alter_categoria_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
