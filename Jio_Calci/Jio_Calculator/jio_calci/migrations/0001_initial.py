# Generated by Django 4.1.3 on 2022-12-04 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=100, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=100, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=100, max_length=100, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jio_calci.category')),
            ],
        ),
        migrations.CreateModel(
            name='SKuName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=100, max_length=100, null=True)),
                ('productname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jio_calci.product_name')),
            ],
        ),
        migrations.AddField(
            model_name='product_name',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jio_calci.subcategory'),
        ),
    ]
