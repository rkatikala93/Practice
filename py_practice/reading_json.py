import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print("List of people in the space are ")
for people in json['people']:
    print(people['name'])
