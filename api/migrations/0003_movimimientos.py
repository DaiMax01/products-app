# Generated by Django 5.1.4 on 2024-12-10 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_producto_cantidad_producto_costo_unitario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'ENTRADA'), (2, 'SALIDA')])),
                ('cantidad', models.BigIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='api.stockproductos')),
            ],
        ),
    ]
