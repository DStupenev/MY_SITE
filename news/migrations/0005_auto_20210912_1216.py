# Generated by Django 3.2.5 on 2021-09-12 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210908_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=150, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
        ),
    ]