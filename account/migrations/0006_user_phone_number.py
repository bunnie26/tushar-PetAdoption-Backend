# Generated by Django 4.2.4 on 2023-11-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=None, max_length=15, null=True),
        ),
    ]
