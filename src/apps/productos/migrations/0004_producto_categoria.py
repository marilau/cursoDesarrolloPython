# Generated by Django 3.2.9 on 2021-12-05 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos_relacionados', to='productos.categoria'),
        ),
    ]
