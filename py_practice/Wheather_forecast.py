import requests
api = "7f71ec851a6c1bebc08301584d57a2db"
url = "http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid="+api+""
request = requests.get(url)
json = request.json()

for data in json["weather"]:
    print("Today's weather forecast is ", data["description"], sep='')
temp_max = json.get("main").get("temp_max")
print("Today's maximum temperature is :", temp_max)
print("Today's minimum temperature is :", json["main"]["temp_min"])
