# Generated by Django 3.1 on 2020-08-23 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='views')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='Pub_date')),
                ('top_fixed', models.BooleanField(default=False, verbose_name='Top_fixed')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Writer')),
            ],
            options={
                'verbose_name': 'Notice',
                'verbose_name_plural': 'Notice',
                'db_table': 'Notice',
            },
        ),
    ]
