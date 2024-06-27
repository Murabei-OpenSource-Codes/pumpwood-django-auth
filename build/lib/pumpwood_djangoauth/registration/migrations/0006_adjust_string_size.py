# Generated by Django 3.2.6 on 2024-01-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_initial_mfa_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pumpwoodmfacode',
            name='code',
            field=models.CharField(blank=True, help_text='6 digit MFA code', max_length=6),
        ),
        migrations.AlterField(
            model_name='pumpwoodmfamethod',
            name='mfa_parameter',
            field=models.CharField(blank=True, help_text='MFA Parameter. Telephone, email, etc...', max_length=200),
        ),
        migrations.AlterField(
            model_name='pumpwoodmfarecoverycode',
            name='code',
            field=models.CharField(blank=True, help_text='8 digits recovery code', max_length=8),
        ),
    ]
