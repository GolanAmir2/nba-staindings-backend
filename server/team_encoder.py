import sys
sys.path.append('C:\\Users\\Amirgol\\courses\\python\\NBA_to_the_max')
from data_scrap.team import Team
import json

class TeamEncoder(json.JSONEncoder):
	def default(self, to_encode):
		if isinstance(to_encode, Team):
			team_to_encode = to_encode
			return { "team" : team_to_encode.name, "wins" : team_to_encode.wins, "loses" : team_to_encode.loses, "playoff" : team_to_encode.playoff, "color": team_to_encode.color }
		else:
			super().default(to_encode)