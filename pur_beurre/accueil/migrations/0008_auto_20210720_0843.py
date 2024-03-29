# Generated by Django 3.2.5 on 2021-07-20 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0007_db_product_image_small_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_product',
            name='code',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='db_product',
            name='category_id',
            field=models.ManyToManyField(to='accueil.Category_db'),
        ),
    ]
