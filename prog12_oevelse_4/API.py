#API.py
import requests

def fetch_elspot():
    elspot = requests.get(
        url = "https://api.energidataservice.dk/dataset/Elspotprices?limit=2")

    APIelpris = elspot.json().get('records')[1].get('SpotPriceDKK')
    #print("Elpris lige nu: " ,APIelpris)
    return APIelpris

def fetch_CO2Emis():
    emis = requests.get(
        url = "https://api.energidataservice.dk/dataset/CO2Emis?limit=2")

    APIco2 = emis.json().get('records')[1].get('CO2Emission')
    #print("CO2 g pr. kwh : " ,APIco2)
    return APIco2