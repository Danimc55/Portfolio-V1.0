# Generated by Django 3.2.8 on 2021-11-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='app\\%y'),
        ),
    ]
