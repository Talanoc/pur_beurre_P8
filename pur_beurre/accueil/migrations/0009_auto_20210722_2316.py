# Generated by Django 3.2.5 on 2021-07-22 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accueil', '0008_auto_20210720_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.BigIntegerField(unique=True)),
                ('url', models.URLField()),
                ('product_name', models.CharField(max_length=200)),
                ('nutriscore_grade', models.CharField(max_length=2)),
                ('image_url', models.URLField()),
                ('image_small_url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='favorite_db',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='favorite_db',
            name='id_user',
        ),
        migrations.RenameModel(
            old_name='Category_db',
            new_name='Category',
        ),
        migrations.DeleteModel(
            name='Db_product',
        ),
        migrations.DeleteModel(
            name='Favorite_db',
        ),
        migrations.DeleteModel(
            name='User_db',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='accueil.Category'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.product'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
