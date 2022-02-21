# Generated by Django 4.0.1 on 2022-02-17 04:38

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
                ('name', models.CharField(default=None, max_length=300)),
                ('category_image', models.ImageField(default=None, upload_to='category')),
                ('category_description', models.TextField(default=None, max_length=500)),
                ('margin_top', models.CharField(choices=[('mt-30', 'mt-30'), ('mt-85', 'mt-85')], default='mt-30', max_length=100)),
                ('slug', models.SlugField(default=None, max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, default=None, max_length=200)),
                ('product_description', models.TextField(blank=True, default=None, max_length=500)),
                ('product_ingridient', models.CharField(blank=True, default=None, max_length=400)),
                ('product_highlights', models.TextField(blank=True, default=None, max_length=500)),
                ('product_features', models.TextField(blank=True, default=None, max_length=500)),
                ('product_image_1', models.ImageField(default=None, upload_to='products')),
                ('product_image_2', models.ImageField(blank=True, default=None, upload_to='products')),
                ('product_image_3', models.ImageField(blank=True, default=None, upload_to='products')),
                ('product_image_4', models.ImageField(blank=True, upload_to='products')),
                ('product_image_5', models.ImageField(blank=True, upload_to='products')),
                ('product_image_6', models.ImageField(blank=True, upload_to='products')),
                ('slug', models.SlugField(default=None, max_length=100)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutrition_information', models.CharField(blank=True, default=None, max_length=200)),
                ('for_100gm', models.CharField(blank=True, default=None, max_length=200)),
                ('for_16gm', models.CharField(blank=True, default=None, max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]