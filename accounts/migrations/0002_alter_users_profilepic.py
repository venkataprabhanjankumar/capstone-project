# Generated by Django 4.1.2 on 2022-10-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profilePic',
            field=models.FileField(storage='profilePics', upload_to=''),
        ),
    ]