# Generated by Django 3.2.9 on 2021-12-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_producto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tags',
            field=models.ManyToManyField(to='productos.Tag'),
        ),
    ]