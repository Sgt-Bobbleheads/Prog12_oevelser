import requests
# Denne handling kræver at ESP32 har internetforbindelse

response = requests.get(
    url='https://api.energidataservice.dk/dataset/CO2Emis?limit=2')

result = response.json()

for k, v in result.items():
    print(k, v)

records = result.get('records', [1])

print('records:')
for record in records:
    print(' ', record)
    
print(response.json().get("records")[1].get("PriceArea"))