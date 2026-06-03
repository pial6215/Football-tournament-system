from django.db import models

# Doler Tothyo
class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Khelar Tothyo
class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    
    # Khela shuru howar age score faka thakbe, tai null=True, blank=True
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team1.short_name} vs {self.team2.short_name}"