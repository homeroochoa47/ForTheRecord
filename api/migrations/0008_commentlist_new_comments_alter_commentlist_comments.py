# Generated by Django 4.1.3 on 2022-12-28 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_comment_list_commentlist_comments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentlist',
            name='new_comments',
            field=models.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='commentlist',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]
