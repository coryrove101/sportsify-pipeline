import requests
import sportsipy as sp
from sportsipy.ncaab.teams import Teams

'''class SportsifyClient:
    BASE_URL = "https://api.sportsify.com"

    def __init__(self):
        pass

    def get_sports_data(self, sport_type):
        url = f"{self.BASE_URL}/sports/{sport_type}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_all_sports(self):
        url = f"{self.BASE_URL}/sports"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
'''
            

def get_height_in_inches(height):
    feet, inches = height.split('-')
    return int(feet) * 12 + int(inches)

def print_tallest_player(team_heights):
    tallest_player = max(team_heights, key=team_heights.get)
    print('%s: %s in.' % (tallest_player, team_heights[tallest_player]))

for team in Teams():
    print('=' * 80)
    print(team.name)
    team_heights = {}
    for player in team.roster.players:
        height = get_height_in_inches(player.height)
        team_heights[player.name] = height
    print_tallest_player(team_heights)

    from sportsipy.ncaab.schedule import Schedule

    purdue_schedule = Schedule('purdue')
    for game in purdue_schedule:
        print(game.date)