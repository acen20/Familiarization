# Generated by Django 3.2.4 on 2021-06-20 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_quotes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotes',
            old_name='text',
            new_name='qtext',
        ),
    ]
