# Generated by Django 3.2.7 on 2021-11-14 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('street_address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(blank=True)),
                ('story', models.TextField(blank=True)),
                ('web_link', models.CharField(max_length=200, null=True)),
                ('image', models.TextField(blank=True)),
                ('fields', models.CharField(max_length=350, null=True)),
                ('motivations', models.CharField(max_length=350, null=True)),
            ],
        ),
    ]