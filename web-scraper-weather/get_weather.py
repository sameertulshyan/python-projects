from bs4 import BeautifulSoup
import requests

input = requests.get('https://weather.com/weather/today/l/USNY0996:1:US')
data = BeautifulSoup(input.text, 'html.parser')

weather = (data.find("div", class_="today_nowcard-temp").text)

print("The temperature in New York today is " + weather)