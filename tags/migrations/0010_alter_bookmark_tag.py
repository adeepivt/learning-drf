# Generated by Django 3.2.6 on 2021-08-31 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0009_auto_20210831_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='tag',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tags.tag'),
        ),
    ]
