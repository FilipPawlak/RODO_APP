# Generated by Django 3.1.3 on 2020-12-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN_FORM', '0004_auto_20201205_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainform',
            name='ZgodaDaneOsobowe',
        ),
        migrations.AddField(
            model_name='mainform',
            name='ZgodaInfHandlowa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mainform',
            name='ZgodaMarketing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mainform',
            name='ZgodaMarketingBezp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mainform',
            name='ZgodaPrzeglad',
            field=models.BooleanField(default=False),
        ),
    ]
