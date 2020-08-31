# Generated by Django 3.1 on 2020-08-31 03:23

from django.db import migrations, models
import notice.models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='filename',
            field=models.CharField(max_length=64, null=True, verbose_name='첨부파일명'),
        ),
        migrations.AddField(
            model_name='notice',
            name='upload_files',
            field=models.FileField(blank=True, null=True, upload_to=notice.models.get_file_path, verbose_name='파일'),
        ),
    ]
