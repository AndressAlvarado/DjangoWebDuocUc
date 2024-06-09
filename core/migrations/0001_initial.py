# Generated by Django 5.0.1 on 2024-05-29 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_producto',
            fields=[
                ('id_tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('imagen', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
                ('id_tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo_producto')),
            ],
        ),
    ]