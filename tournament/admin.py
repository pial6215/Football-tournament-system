from django.contrib import admin
from .models import Team, Match

# Amader toiri kora model gulo admin panel e register korlam
admin.site.register(Team)
admin.site.register(Match)