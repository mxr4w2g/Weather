import requests #fetch weather api

api_key = '97c02aa47847c479de3aaaecaee27c0b' #variable called api_key and contains api key into a string 


user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}") #this variable uses request library and fetch this url

weather = weather_data.json()['weather'][0]['main']
temp =  weather_data.json()['main']['temp']

print(weather,temp)