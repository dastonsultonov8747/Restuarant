# Generated by Django 5.1.5 on 2025-01-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_bigmenu_icon_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(max_length=600, upload_to='Slider/')),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
