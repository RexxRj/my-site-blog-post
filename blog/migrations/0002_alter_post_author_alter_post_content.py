# Generated by Django 5.1.4 on 2025-01-01 08:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]
