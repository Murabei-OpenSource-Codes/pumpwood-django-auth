# Generated by Django 3.2.6 on 2023-12-28 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metabase', '0008_model_class_column_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metabasedashboard',
            name='is_static',
        ),
    ]