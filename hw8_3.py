import requests

url = "https://api.stackexchange.com/2.3/questions"
params = {"fromdate":"1635638400", "todate":"1635811200",
          "order" : "desc", "sort" : "activity", "site" : "stackoverflow"}

resp = requests.get(url = url, params=params)
result = resp.json()

for i in result['items']:
    for j in i['tags']:
        if 'python' in j:
            print(i)


