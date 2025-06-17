import requests

response = requests.get('https://status.digitalocean.com/api/v2/status.json')
print(response.json()['status']['description'])

# it will give us a big dictionary
