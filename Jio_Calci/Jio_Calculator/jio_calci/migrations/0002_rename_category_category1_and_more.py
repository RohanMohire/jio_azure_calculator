# Generated by Django 4.1.3 on 2022-12-05 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jio_calci', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Category1',
        ),
        migrations.RenameModel(
            old_name='Product_Name',
            new_name='Product_Name1',
        ),
        migrations.RenameModel(
            old_name='SKuName',
            new_name='SKuName1',
        ),
        migrations.RenameModel(
            old_name='SubCategory',
            new_name='SubCategory1',
        ),
    ]
