from django.db import models
from account.models import User
class Pet(models.Model):
    PET_TYPES = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('rabbit', 'Rabbit'),
        # Add more types as needed
    )
    PET_SIZE = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('xl', 'ExtraLarge'),
    )

    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=20, choices=PET_TYPES)
    age = models.IntegerField()
    size = models.CharField(max_length=20, choices=PET_SIZE)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.URLField()
    available_for_adoption = models.BooleanField(default=True)
    adopted = models.BooleanField(default=False)
    # Add more fields as required
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_pets', null=True, default=None)
    
