# Generated by Django 5.1 on 2024-09-11 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterField(
            model_name='testproduct',
            name='available',
            field=models.BooleanField(default=True, verbose_name='В наличии'),
        ),
        migrations.AlterField(
            model_name='testproduct',
            name='stock',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество на складе'),
        ),
        migrations.AddField(
            model_name='testproduct',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.testcategory'),
        ),
    ]
