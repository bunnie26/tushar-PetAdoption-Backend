# Generated by Django 4.2.4 on 2023-11-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_remove_pet_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='detailed_description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='pet',
            name='donation_reason',
            field=models.TextField(default=None),
        ),
    ]