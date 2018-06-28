from django.contrib import admin
from .models import Character

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    model = Character
    list_display = ["first_name", "last_name", "age", "status"]

admin.site.register(Character, CharacterAdmin)