# Generated by Django 5.1.4 on 2024-12-09 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='producto',
            name='costo_unitario',
            field=models.DecimalField(decimal_places=4, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_venta',
            field=models.DecimalField(decimal_places=4, max_digits=14, null=True),
        ),
        migrations.CreateModel(
            name='StockProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_disponible', models.BigIntegerField(default=0)),
                ('valor_total', models.DecimalField(decimal_places=4, max_digits=14)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='api.producto')),
            ],
        ),
    ]
