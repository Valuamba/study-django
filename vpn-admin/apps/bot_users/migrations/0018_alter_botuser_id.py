# Generated by Django 3.2.7 on 2022-09-08 14:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0017_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('27d0fede-01b6-4ecd-a2bf-5a79dc84a773'), editable=False),
        ),
    ]
