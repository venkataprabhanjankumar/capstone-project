# Generated by Django 4.1.2 on 2022-10-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_users_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profilePic',
            field=models.FileField(upload_to='profilePics'),
        ),
    ]
