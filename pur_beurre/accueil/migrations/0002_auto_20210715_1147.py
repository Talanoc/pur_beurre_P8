# Generated by Django 3.2.5 on 2021-07-15 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='db_product',
            old_name='imageurl',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='user_db',
            old_name='userpw',
            new_name='user_pw',
        ),
    ]
