# Generated by Django 2.2.3 on 2019-07-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchers', '0003_profilemodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
