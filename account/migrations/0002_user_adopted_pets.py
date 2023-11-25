# Generated by Django 4.2.5 on 2023-11-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_remove_pet_adopted_pets'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adopted_pets',
            field=models.ManyToManyField(related_name='adopted_by', to='pets.pet'),
        ),
    ]
