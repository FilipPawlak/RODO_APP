# Generated by Django 3.1.3 on 2021-01-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN_FORM', '0006_auto_20201214_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainform',
            name='NumerZlecenia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
