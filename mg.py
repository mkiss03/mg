import requests

# API kulcs
api_key = "83zcrpy2mxcw2xc2rda58h9q"

# Az API végpontja
base_url = "https://api.sportradar.us/soccer/trial/v4/en/competitions/sr:competition:17/info.json"

# Az API kérés paraméterei
params = {
    "api_key": api_key
}

try:
    # API kérés elküldése
    response = requests.get(base_url, params=params)

    # Válasz ellenőrzése
    response.raise_for_status()

    # Válasz JSON adatokká alakítása
    data = response.json()

    # A válaszban található verseny információk kiíratása
    print("Verseny neve:", data["competition"]["name"])
    print("Verseny azonosítója:", data["competition"]["id"])
    print("Verseny kategóriája:", data["competition"]["category"]["name"])
    print("Verseny kategóriájának országkódja:", data["competition"]["category"]["country_code"])

except requests.exceptions.RequestException as e:
    # Hiba esetén kiírjuk a hibaüzenetet
    print("Hiba történt az API-híváskor:", e)
