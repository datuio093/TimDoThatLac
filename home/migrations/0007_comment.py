# Generated by Django 4.1.1 on 2022-12-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_mypost_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.TextField(null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]