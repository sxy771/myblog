# Generated by Django 3.1 on 2020-08-31 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='이름'),
        ),
    ]