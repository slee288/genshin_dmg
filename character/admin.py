from django.contrib import admin
from character.models import Character

# Register your models here.
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name",]

admin.site.register(Character, CharacterAdmin)