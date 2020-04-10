import unittest
import sys
sys.path.append('C:\\Users\\Amirgol\\courses\\python\\NBA_to_the_max')
from data_scrap.main import scrap
from data_scrap.parse import parse_html
from data_scrap.parse import parse_champion
from data_scrap.team import Team
from server.team_encoder import TeamEncoder
import json
from bs4 import BeautifulSoup


class DataScrapTests(unittest.TestCase):
    def test_invalid_day_raise_exception(self):
        self.assertRaises(ValueError, scrap, 2001, 1, 0, {})

    def test_parse(self):
        filename = "C:\\Users\\Amirgol\\courses\\python\\NBA_to_the_max\\tests\\resources\\month=2&day=22&year=2000&lg_id=NBA.html"
        file = open(filename, "r")
        soup = BeautifulSoup(file, 'html.parser')
        teams =  parse_html(soup, {})
        dump = json.dumps(teams, cls=TeamEncoder).encode('utf-8')


    def test_dump(self):
    	team = Team("name", 1 , 2 , False, "red")
    	dump = json.dumps(team, cls=TeamEncoder).encode('utf-8')

    def test_champion_parse(self):
        filename = "C:\\Users\\Amirgol\\courses\\python\\NBA_to_the_max\\tests\\resources\\testchampionpage.html"
        file = open(filename, "r")
        soup = BeautifulSoup(file, 'html.parser')
        champion =  parse_champion(soup)
        #dump = json.dumps(champion).encode('utf-8')
        print(champion)


