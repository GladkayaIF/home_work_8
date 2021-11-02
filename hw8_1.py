import requests

url = 'https://superheroapi.com/api/2619421814940190/search/'
super_hero = ['Hulk', 'Captain America', 'Thanos']

hero_power = {}
for hero in super_hero:
    search = url + hero
    resp = requests.get(search)
    result = resp.json()['results']
    for i in result:
        if i['name'] == hero:
            hero_power[hero] = i['powerstats']['intelligence']

most_intellehge = sorted(hero_power.values())
for most in hero_power:
    if hero_power[most] == most_intellehge[0]:
        print('Самый умный супергерой ' + most +' из ' + str(super_hero))
