# Generated by Django 3.2.6 on 2023-12-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metabase', '0009_drop_is_static'),
    ]

    operations = [
        migrations.AddField(
            model_name='metabasedashboard',
            name='auto_embedding',
            field=models.BooleanField(default=False),
        ),
    ]