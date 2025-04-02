import requests

ride = {
	"PULocationID": 10,
	"DOLocationID": 15,
	"trip_distance": 15
}

url = 'http://localhost:9696'

response = requests.post(f"{url}/predict", json=ride)
print(response.json)
print(response)
print(response.content)