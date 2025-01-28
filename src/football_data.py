import requests
import json
from constants import URI, API_TOKEN
from utils import filter_dict2str

head = {
	"X-Auth-Token": API_TOKEN,
	"X-Unfold-Goals": "true"
}

def get(url):
	"""
	Wrapper for get request to football data api.

	Args:
		url (string): the url of the get request
	
	Returns:
		dict: the dictionary representation of the response content from the request
	"""
	print(f"Sending request {url}")
	return json.loads(requests.get(url, headers=head).content)

def get_area(id=None):
	"""
	Get area by id, or all areas if no id provided.

	Args:
		id (int|None): id of area being requested

	Returns:
		dict: area response as a dictionary
	"""
	if (id):
		response = get(f"{URI}/areas/{id}")
	else:
		response = get(f"{URI}/areas")
	return response

def get_comp(competition=None, filters=None):
	"""
	Get competition by id or code (e.g. "PL" for Premier League), or all comps if no value provided.

	Args:
		competition (int|string|None): id or code of competition being requested
		filters (dict|None): dictionary of optional filters. Accepted key/value pairs:
			areas={AREAS} - filter by area id
						  - e.g. get_comp(None, {'areas': 2224}) ->
								"http://api.football-data.org/v4/competitions?areas=2224" for competitions in Spain
						  - can also use an array
						  - e.g. get_comp(None, {'areas': [2081, 2072]}) ->
								"http://api.football-data.org/v4/competitions?areas=2224,2072" for competitions in France and England

	Returns:
		dict: competition response as a dictionary
	"""
	filter_string = filter_dict2str(filters)
	if (competition):
		response = get(f"{URI}/competitions/{competition}")
	else:
		response = get(f"{URI}/competitions?{filter_string}")
	return response

def get_comp_standings(id, filters=None):
	"""
	Get competition standings by comp id.

	Args:
		id (int): id of competition being requested
		filters (dict|None): dictionary of optional filters. Accepted key/value pairs:
			matchday={MATCHDAY} - filter by matchday
								- e.g. get_comp_standings(2021, {'matchday': 15, 'season': 2023}) ->
									"http://api.football-data.org/v4/competitions/2021/standings?matchday=15&season=2023" for the Premier League standings at matchday 15 of the 2023/24 season
								- only seems to work when paired with "season"
			season={YEAR} - filter by year season began in (example above)
			date={DATE} - get standings at specified date e.g. get_comp_standings(2021, {'date': '2025-01-01'}) ->
							"http://api.football-data.org/v4/competitions/2021/standings?date=2025-01-01" for the Premier League standings on new years day 2025

	Returns:
		dict: standings response as a dictionary
	"""
	filter_string = filter_dict2str(filters)
	response = get(f"{URI}/competitions/{id}/standings?{filter_string}")
	return response

def get_comp_matches(id, filters=None):
	"""
	Get competition matches by comp id.

	Args:
		id (int): id of competition being requested
		filters (dict|None): dictionary of optional filters. Accepted key/value pairs:
			dateFrom={DATE} - get matches that took place after a specified date
							- e.g. get_comp_standings(2021, {'dateFrom': '2025-01-01', 'dateTo': '2025-01-31'}) ->
								"http://api.football-data.org/v4/competitions/2021/matches?dateFrom=2025-01-01&dateTo=2025-31-01" for matches in the Premier League in January 2025
			dateTo={DATE} - get matches that took place before a specified date (example above)
			matchday={MATCHDAY} - filter by matchday e.g. get_comp_standings(2021, {'matchday': 15, 'season': 2023}) -> "http://api.football-data.org/v4/competitions/2021/standings?matchday=15&season=2023" for the standings at matchday 15 of the 2023/24 season
								- only seems to work when paired with "season"
			season={YEAR} - filter by year season began in (example above)

	Returns:
		dict: matches response as a dictionary
	"""
	filter_string = filter_dict2str(filters)
	response = get(f"{URI}/competitions/{id}/standings?{filter_string}")
	return response