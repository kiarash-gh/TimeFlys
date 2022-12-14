# Generated by Django 4.1.2 on 2022-10-10 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('web_url', models.URLField(blank=True, null=True)),
                ('job_title', models.CharField(max_length=255)),
                ('discription', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
