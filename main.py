import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("RC_API_KEY")

url = "https://api.restcountries.com/countries/v5/name"

ulke_adi = input("Ülke adı girin: ")

response = requests.get(url,params={"q": ulke_adi},headers={"Authorization": f"Bearer {api_key}"})

print(response.status_code)
data = response.json()

ulke = data["data"]["objects"][0]
print(f"Name(Adı): {ulke["names"]["common"]}")
print(f"Flag(Bayrak): {ulke["flag"]["emoji"]}")
print(f"Capital(Başkent): {ulke["capitals"][0]["name"]}")
print(f"Population(Nüfus): {ulke["population"]}")
print(f"Language(Dil): {ulke["languages"][0]["name"]}")
print(f"Currency(Para Birimi): {ulke["currencies"][0]["name"]}")
