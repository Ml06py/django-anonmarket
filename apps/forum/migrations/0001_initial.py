# Generated by Django 4.1 on 2022-08-30 11:04

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
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('closed', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('allowed_members', models.ManyToManyField(blank=True, related_name='forum_allowed_members', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]