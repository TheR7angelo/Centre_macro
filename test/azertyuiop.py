import requests


url = "https://api.flaticon.com/v3/app/authentication"
payload = "apikey=4857a47f7d6ee8b4fff95628639f0b8bc4b9ffc1"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "api.flaticon.com",
    'x-rapidapi-key': "493dc97948msh3d99bd78295a935p129a58jsn6644d99348d1"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)
