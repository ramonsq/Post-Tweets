import requests
import json

# Devuelve informacion del usuario que le meta
url = "https://api.twitter.com/2/tweets/search/recent?query={your_tw_account}"

payload={}
headers = {
  'Cookie': 'guest_id=v1%3A167269726562318385'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Mandamos un tweet
url = "https://api.twitter.com/2/tweets"

payload = json.dumps({
  "text": "Hello World! este es mi tercer tweet"
})
headers = {
  'Authorization': '', #aqui cada uno pone el suyo
  'Content-Type': 'application/json',
  'Cookie': 'guest_id=v1%3A167269726562318385'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)






