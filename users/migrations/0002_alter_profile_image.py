# Generated by Django 3.2.7 on 2021-09-26 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='645299.jpg', upload_to='profile_pics'),
        ),
    ]
