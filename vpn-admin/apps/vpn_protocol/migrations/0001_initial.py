# Generated by Django 3.2.7 on 2022-08-25 23:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VpnProtocol',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('protocol', models.CharField(choices=[('wireguard', 'Wireguard'), ('open_vpn', 'OpenVPN')], max_length=154, unique=True)),
                ('is_default', models.BooleanField(default=False, verbose_name='Is default')),
            ],
            options={
                'db_table': 'vpn_protocols',
            },
        ),
    ]
