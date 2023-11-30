# Generated by Django 4.2.4 on 2023-11-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0009_remove_pet_detailed_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='donation_reason',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='vaccination',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
