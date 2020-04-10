from http.server import BaseHTTPRequestHandler
import json
import sys
sys.path.append('C:\\Users\\Amirgol\\courses\\python\\NBA_to_the_max')
from data_scrap.main import scrap_team_midyear
from data_scrap.main import scrap_team_endyear
from data_scrap.main import scrap_champion
from team_encoder import TeamEncoder

class HTTPServer_handler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()
		content = self.respond()
		self.wfile.write(content)
		return

	def do_POST(self):
		return

	def handle_http(self, status, content_type):
		path = self.path[1:]
		content=""
		if(str.isdigit(path)):
			year = int(path)
			mid_year_standings = scrap_team_midyear(year, 2, 22);
			end_year_standings = scrap_team_endyear(year, 4, 20, mid_year_standings);
			champion = scrap_champion(year)
			content = { "midSeason" : mid_year_standings, "endSeason" : end_year_standings, "champion": champion }
		return json.dumps(content, cls=TeamEncoder).encode('utf-8')

	def respond(self):
		content = self.handle_http(200, 'text/html')
		return content
