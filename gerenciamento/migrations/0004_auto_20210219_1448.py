# Generated by Django 3.1.7 on 2021-02-19 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0003_auto_20210219_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='afericao',
            old_name='qtd',
            new_name='quantidade',
        ),
    ]
