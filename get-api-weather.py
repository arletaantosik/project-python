import requests

def get_weather(city, units='metric', api_key='26631f0f41b95fb9f5ac0df9a8f43c92'): #metric - celcius, api_key generated when create an acount on openweathermap
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}" #weather for 5 days, generated every 3h, 40 rows (5*8)
  r = requests.get(url)
  content = r.json() # transform to dict (slownik)
  with open('data.txt', 'a') as file: # opens data.txt, 'a' - append mode, if the file doesn't exist, it will be created
    for dicty in content['list']:
      file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n") #first element in array

print(get_weather(city='Washington'))
