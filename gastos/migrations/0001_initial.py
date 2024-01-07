# Generated by Django 5.0 on 2024-01-02 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0003_categoria_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obs', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('grupo', models.IntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('fk_categorias', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria')),
            ],
        ),
    ]
