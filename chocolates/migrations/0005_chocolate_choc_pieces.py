# Generated by Django 3.2.25 on 2024-05-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocolates', '0004_auto_20240525_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='chocolate',
            name='choc_pieces',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
