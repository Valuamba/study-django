# Generated by Django 3.2.7 on 2022-09-06 18:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0014_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a6c9ebe2-b46d-4c52-81fa-31572a5bf054'), editable=False),
        ),
    ]
