# Generated by Django 4.0.5 on 2022-06-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_myuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
