# Generated by Django 3.1.6 on 2021-02-05 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20210205_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatrecord',
            old_name='consumer',
            new_name='client',
        ),
    ]
