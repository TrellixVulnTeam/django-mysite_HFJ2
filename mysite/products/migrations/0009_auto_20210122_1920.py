# Generated by Django 3.1.5 on 2021-01-22 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210120_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id', 'code', 'name', 'specification', 'size'), 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
    ]
