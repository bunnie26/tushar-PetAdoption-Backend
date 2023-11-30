# Generated by Django 4.2.4 on 2023-11-30 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0005_alter_pet_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='detailed_description',
            field=models.TextField(default=None, null=True),
        ),
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
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_pets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pet',
            name='vaccination',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
