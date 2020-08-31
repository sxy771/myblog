# Generated by Django 3.1 on 2020-08-31 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice', '0002_auto_20200831_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='댓글내용')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.notice', verbose_name='게시글')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='댓글작성자')),
            ],
            options={
                'verbose_name': '자유게시판 댓글',
                'verbose_name_plural': '자유게시판 댓글',
                'db_table': '자유게시판 댓글',
            },
        ),
    ]