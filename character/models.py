from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length = 10)
    attack = models.IntegerField()
    skill_percentage = models.FloatField("Skill Percentage")
    add_damage = models.FloatField("Additional Percentage")
    crit_dmg = models.FloatField("Crit Damage")

    def destructure_stats(self):
        return self.attack, self.skill_percentage, self.add_damage, self.crit_dmg