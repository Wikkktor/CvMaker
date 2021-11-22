# Generated by Django 3.2.9 on 2021-11-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100, null=True)),
                ('street', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('link', models.TextField()),
                ('company', models.CharField(max_length=255)),
                ('function', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('started', models.DateField()),
                ('ended', models.DateField(null=True)),
                ('school', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('skill', models.TextField()),
            ],
        ),
    ]