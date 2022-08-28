# Generated by Django 4.1 on 2022-08-28 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(choices=[('l', 'Like'), ('d', 'Dislike')], default='l', max_length=1)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_rate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
