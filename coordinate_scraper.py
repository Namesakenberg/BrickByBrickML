import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

from jinja2.filters import ignore_case

base_url = 'https://www.google.com/search?q='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def get_coordinates(sector):
    search_term = f"sector {sector} gurgaon coordinates"
    response = requests.get(base_url + search_term , headers=headers)
    if response.status_code==200:
        soup = BeautifulSoup(response.content,'html.parser')
        coordinates_div = soup.find("div",class_="Z0LcW t2b5cf")
        if coordinates_div:
            return coordinates_div.text
    return None
df = pd.DataFrame(columns = ["Sector" , "Coordinates"])

for sector in range(1,116):
    coordinates = get_coordinates(sector)
    df = df.append({"sector":f"Sector {sector}","coordinates":coordinates},ignore_index=True)
df.to_csv("latlong",index=False)
