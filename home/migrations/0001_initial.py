# Generated by Django 4.1.1 on 2022-11-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mypost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('type', models.TextField()),
                ('object', models.TextField()),
                ('descrip', models.TextField()),
                ('address', models.TextField()),
                ('name', models.TextField()),
                ('pnum', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
    ]
