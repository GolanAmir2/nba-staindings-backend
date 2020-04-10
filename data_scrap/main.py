import requests
from data_scrap.validate_date import validate_date
from data_scrap.parse import parse_html_midyear

from data_scrap.parse import parse_html_endyear
from data_scrap.parse import parse_champion
from bs4 import BeautifulSoup
import constants
base_url = "https://www.basketball-reference.com/friv/standings.fcgi?"
champion_url = "https://www.basketball-reference.com/playoffs"



def scrap_team_midyear(year, month, day):
	soup = create_soup(year,month,day)
	return parse_html_midyear(soup)
def scrap_team_endyear(year, month, day, midyear_standings):
	soup = create_soup(year,month,day)
	return parse_html_endyear(soup, midyear_standings)

def create_soup(year, month, day):
	validate_date(year, month, day)
	url = f"{base_url}month={month}&day={day}&year={year}&lg_id=NBA"
	request = get_html(url)
	return get_soup(request)

def scrap_champion(year):
	url = f"{champion_url}/NBA_{year}.html"
	request = get_html(url)
	soup = get_soup(request)
	return parse_champion(soup)

def get_html(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		print(connectionErrorMessage)

def get_soup(url):
	return BeautifulSoup(url.content, 'html.parser')




