import sys
sys.path.append('C:\\Users\\Amirgol\\courses\\python\\NBA_to_the_max\\data_scrap')
from data_scrap.team import Team
from collections import OrderedDict

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'gray', 'orange', 'purple']
num_of_playoff_teams = 8


def parse_html_midyear(soup):
	print("\nparsing mid year")
	east_table = extract_table(soup, 'e')
	west_table = extract_table(soup, 'w')
	east_teams = create_midyear_teams(east_table)
	west_teams = create_midyear_teams(west_table)
	return {"east" : east_teams, "west" : west_teams}

def parse_html_endyear(soup, mid_year_standings):
	print("\nparsing end year")
	east_table = extract_table(soup, 'e')
	west_table = extract_table(soup, 'w')
	east_teams = create_endyear_teams(east_table, mid_year_standings.get("east"))
	west_teams = create_endyear_teams(west_table, mid_year_standings.get("west"))
	return {"east" : east_teams, "west" : west_teams}

def extract_table(soup, conference):
	standings = soup.select_one('#standings_' + conference)
	return standings.select('.full_table')



def parse_champion(soup):
	print("\nparse champion")
	champ_info = soup.select_one('.playoffs')
	all_links = champ_info.find_all('a')
	champ_team = all_links[4].get_text()
	champ_mvp = all_links[5].get_text()
	return {"champTeam" : champ_team , "champMVP" : champ_mvp }


def create_midyear_teams(table):
	teams = create_teams(table)
	return add_color_midyear(teams)

def create_endyear_teams(table, mid_year_teams):
	teams = create_teams(table)
	return add_color_endyear(teams, mid_year_teams)


def create_teams(table):
	teams = []
	for i in table:
		team_name = i.select_one('th').text.strip()
		team_wins = i.select('td')[0].text.strip()
		team_loses = i.select('td')[1].text.strip()
		playoff = False
		color = ''
		if(team_name[len(team_name)-1] == "*"):
			playoff = True
			team_name = team_name[0:len(team_name)-1] 
		teams.append(Team(team_name, team_wins, team_loses, playoff, color))
	return sort_teams(teams)

def sort_teams(team):
	return sorted(team, key=lambda team: int(team.wins), reverse=True)

def add_color_endyear(teams, mid_year_teams):
	for mid_year_team in mid_year_teams:		
		for team in teams:
			if mid_year_team.name == team.name:
				team.color = mid_year_team.color 
	return teams


def add_color_midyear(teams):
	for i in range(0, num_of_playoff_teams):
		if i < num_of_playoff_teams:
			teams[i].color = colors[i]
	return teams
