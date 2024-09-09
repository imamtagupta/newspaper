# Generated by Django 5.1.1 on 2024-09-09 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_author_category_alter_article_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.author'),
        ),
    ]
