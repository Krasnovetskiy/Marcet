# Generated by Django 4.2 on 2023-04-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('sku', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
