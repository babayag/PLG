# Generated by Django 2.1.5 on 2019-04-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_auto_20190409_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='domain',
            new_name='niche',
        ),
        migrations.AddField(
            model_name='search',
            name='location',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]
