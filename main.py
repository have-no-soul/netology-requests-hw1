import requests

api_url = 'https://superheroapi.com/api/'

TOKEN = '2619421814940190'

search_method = '/search/'

heroes_dict = [
	{'name': "Hulk"},
	{'name': "Captain America"},
	{'name': "Thanos"}
]


def get_hero_ids(heroes_dict):
	heroes_id_list = []
	for super_hero in heroes_dict:
		search_name_url = api_url + TOKEN + search_method + super_hero['name']
		get_search_data = requests.get(search_name_url).json()

		for item in get_search_data['results']:
			heroes_id_list.append({
				'name': item['name'],
				'id': item['id']
			})

	return heroes_id_list


def what_hero_smartest(get_hero_ids):
	intelligence_list = []
	for super_hero in get_hero_ids(heroes_dict):
		id_url = api_url + TOKEN + '/' + super_hero['id']
		get_hero_data_by_id = requests.get(id_url).json()

		for k in get_hero_data_by_id.get('powerstats'):
			if k == 'intelligence':
				intelligence_list.append({
					'name': get_hero_data_by_id['name'],
					'intelligence': get_hero_data_by_id.get('powerstats')[k]
				})

	print(f'Самый умный супергерой – {sorted(intelligence_list, key=lambda i: i["intelligence"])[0]["name"]}. '
	      f'Его интеллект равен {sorted(intelligence_list, key=lambda i: i["intelligence"])[0]["intelligence"]}')


what_hero_smartest(get_hero_ids)
