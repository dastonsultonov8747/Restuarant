# Generated by Django 5.1.5 on 2025-01-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_aksiya_tables_rename_smallmenu_product_smallmenu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigmenu',
            name='icon_url',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]
