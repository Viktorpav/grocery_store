# Generated by Django 2.1.3 on 2018-12-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_productinbasket'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
