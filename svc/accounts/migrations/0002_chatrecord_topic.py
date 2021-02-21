# Generated by Django 3.0.10 on 2021-02-21 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatrecord',
            name='topic',
            field=models.ForeignKey(default=39, on_delete=django.db.models.deletion.CASCADE, to='accounts.TopicList'),
            preserve_default=False,
        ),
    ]