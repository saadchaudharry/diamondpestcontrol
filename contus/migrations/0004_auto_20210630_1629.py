# Generated by Django 2.2.7 on 2021-06-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contus', '0003_auto_20210628_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='heading',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, max_length=9999, null=True),
        ),
    ]
