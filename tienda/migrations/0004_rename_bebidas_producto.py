# Generated by Django 4.1.1 on 2023-06-15 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_bebidas_saludable'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bebidas',
            new_name='Producto',
        ),
    ]
