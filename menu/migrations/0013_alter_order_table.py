# Generated by Django 5.1.5 on 2025-02-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.CharField(),
        ),
    ]
