from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'pet_type', 'age', 'size', 'breed', 'available_for_adoption', 'adopted','photo','posted_by')
    list_filter = ('pet_type', 'size', 'available_for_adoption', 'adopted')
    search_fields = ('name', 'breed')
