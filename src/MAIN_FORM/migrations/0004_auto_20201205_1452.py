# Generated by Django 3.1.3 on 2020-12-05 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN_FORM', '0003_mainform_zgoda_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainform',
            old_name='Zgoda_1',
            new_name='ZgodaDaneOsobowe',
        ),
    ]
