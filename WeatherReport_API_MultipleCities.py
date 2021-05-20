# make sure that you create an empty text file and write the names of the cities that you want
# you must do that in order for the weatherstack API to pull in info
import requests

API_KEY = "899eeef85226d9573cd1dd5efc0b5ba0"
WS_URL = "http://api.weatherstack.com/current"

cities = []
with open("cities.txt") as f:
  for line in f:
    cities.append(line.strip())
print(cities)    

for city in cities:
  parameters = {'access_key': API_KEY, 'query': city}
  response = requests.get(WS_URL, parameters)
  js = response.json()

  temperature = js['current'] ['temperature']
  date = js['location'] ['localtime']

  with open(f"{city}.txt", "a") as f:
    f.write(f"{date}, {temperature}\n")
