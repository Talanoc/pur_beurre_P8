# Generated by Django 3.2.5 on 2021-07-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0002_auto_20210715_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite_db',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
