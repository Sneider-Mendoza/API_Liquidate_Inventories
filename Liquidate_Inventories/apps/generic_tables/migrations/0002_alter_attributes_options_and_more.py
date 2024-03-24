# Generated by Django 5.0.3 on 2024-03-23 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic_tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributes',
            options={'verbose_name': 'Atributo', 'verbose_name_plural': 'Atributos'},
        ),
        migrations.AlterModelOptions(
            name='historicalattributes',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Atributo', 'verbose_name_plural': 'historical Atributos'},
        ),
        migrations.AlterModelOptions(
            name='historicalparameter',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Parametro', 'verbose_name_plural': 'historical Parametros'},
        ),
        migrations.AlterModelOptions(
            name='parameter',
            options={'verbose_name': 'Parametro', 'verbose_name_plural': 'Parametros'},
        ),
        migrations.RenameField(
            model_name='historicalparameter',
            old_name='descriptiom',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='parameter',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
