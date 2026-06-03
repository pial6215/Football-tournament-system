from django.shortcuts import render
from .models import Team, Match

def home(request):
    teams = Team.objects.all()
    matches = Match.objects.all().order_by('date_time')
    
    # Proti ta team er jonno analytics calculation dictionary
    team_stats = {
        team.id: {
            'name': team.name,
            'short_name': team.short_name,
            'mp': 0, 'w': 0, 'd': 0, 'l': 0, 'gd': 0, 'pts': 0
        }
        for team in teams
    }
    
    # Match er data analyze kore table update kora
    for match in matches:
        if match.is_finished:
            t1 = match.team1.id
            t2 = match.team2.id
            s1 = match.team1_score
            s2 = match.team2_score
            
            # Match Played count barano
            team_stats[t1]['mp'] += 1
            team_stats[t2]['mp'] += 1
            
            # Goal Difference calculate kora (Team 1 to Team 2)
            team_stats[t1]['gd'] += (s1 - s2)
            team_stats[t2]['gd'] += (s2 - s1)
            
            # Win, Loss, Draw mapping
            if s1 > s2:      # Team 1 jitsi
                team_stats[t1]['w'] += 1
                team_stats[t1]['pts'] += 3
                team_stats[t2]['l'] += 1
            elif s2 > s1:    # Team 2 jitsi
                team_stats[t2]['w'] += 1
                team_stats[t2]['pts'] += 3
                team_stats[t1]['l'] += 1
            else:            # Draw hoise
                team_stats[t1]['d'] += 1
                team_stats[t2]['d'] += 1
                team_stats[t1]['pts'] += 1
                team_stats[t2]['pts'] += 1

    # Points ar GD layout onujayi sorting (Jader points beshi tara upore thakbe)
    sorted_teams = sorted(
        team_stats.values(), 
        key=lambda x: (x['pts'], x['gd']), 
        reverse=True
    )
    
    return render(request, 'tournament/home.html', {
        'teams': sorted_teams, 
        'matches': matches
    })