# Generated by Django 4.1.1 on 2022-12-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_comment_postid'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.TextField(null=True),
        ),
    ]
