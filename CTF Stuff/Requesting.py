import requests

url = "http://challenge.nahamcon.com:30463/guess"
payload = {
    'guess': r'flag{bec42475a614b9c9ba80d0eb7ed258c5}',
}

response = requests.post(url, json=payload)
data = response.json()
emoji_string = data.get("result", "")

for char in payload['guess'][5:-1]:
    print(" " + char, end="")
print() 
for char in emoji_string:
    print(char, end="")
