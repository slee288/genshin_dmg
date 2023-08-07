from django.shortcuts import render
from django.http import HttpResponse
from character.models import Character
import json

# Create your views here.
def get_characters(request):
    character_list = [{ "name": c.name, "dmg": calculate_dmg(c) } for c in Character.objects.all()]
    return HttpResponse(json.dumps(character_list), content_type = "application/json")

def calculate_dmg(character):
    attack, skill_percentage, add_damage, crit_dmg = character.destructure_stats()
    return attack * skill_percentage * (1 + add_damage) * (1 + crit_dmg) * 0.9 * (187 / (187 + 190))