# Generated by Django 3.2.5 on 2021-07-26 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0010_rename_categories_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categories',
        ),
    ]
