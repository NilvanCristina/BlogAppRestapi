# Generated by Django 3.1 on 2021-11-11 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsletter', '0002_auto_20211111_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='email',
            new_name='user_email',
        ),
    ]