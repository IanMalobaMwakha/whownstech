# Generated by Django 2.1 on 2023-03-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('reading_time', models.CharField(max_length=10)),
                ('cover_image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
