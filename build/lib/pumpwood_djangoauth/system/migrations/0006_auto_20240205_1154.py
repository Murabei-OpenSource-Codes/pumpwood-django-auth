# Generated by Django 3.2.6 on 2024-02-05 11:54

from django.db import migrations, models
import pumpwood_communication.serializers


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20240203_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kongroute',
            options={'verbose_name': ('R', 'o', 'u', 't', 'e'), 'verbose_name_plural': ('R', 'o', 'u', 't', 'e', 's')},
        ),
        migrations.AlterModelOptions(
            name='kongservice',
            options={'verbose_name': ('S', 'e', 'r', 'v', 'i', 'c', 'e'), 'verbose_name_plural': ('S', 'e', 'r', 'v', 'i', 'c', 'e', 's')},
        ),
        migrations.AlterField(
            model_name='kongroute',
            name='route_name',
            field=models.CharField(help_text=('N', 'a', 'm', 'e', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'r', 'o', 'u', 't', 'e', ' ', '(', 'm', 'u', 's', 't', ' ', 'b', 'e', ' ', 'u', 'n', 'i', 'q', 'u', 'e', ')'), max_length=100, unique=True, verbose_name=('R', 'o', 'u', 't', 'e', ' ', 'N', 'a', 'm', 'e')),
        ),
        migrations.AlterField(
            model_name='kongservice',
            name='extra_info',
            field=models.JSONField(blank=True, default=dict, encoder=pumpwood_communication.serializers.PumpWoodJSONEncoder, help_text=('O', 't', 'h', 'e', 'r', ' ', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n', ' ', 't', 'h', 'a', 't', ' ', 'c', 'a', 'n', ' ', 'b', 'e', ' ', 'u', 's', 'e', 'f', 'u', 'l', 'l', ' ', 'f', 'o', 'r', ' ', 't', 'h', 'i', 's', ' ', 's', 'e', 'r', 'v', 'i', 'c', 'e'), verbose_name=('E', 'x', 't', 'r', 'a', ' ', 'i', 'n', 'f', 'o', '.')),
        ),
        migrations.AlterField(
            model_name='kongservice',
            name='service_kong_id',
            field=models.TextField(help_text=('I', 'D', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 's', 'e', 'r', 'v', 'i', 'c', 'e', ' ', 'o', 'n', ' ', 'k', 'o', 'n', 'g'), unique=True, verbose_name=('K', 'o', 'n', 'g', ' ', 'I', 'D')),
        ),
    ]
