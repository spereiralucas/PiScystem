# Generated by Django 3.1.7 on 2021-02-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0008_auto_20210219_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afericao',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
