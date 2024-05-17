import requests

url = "https://www.prothomalo.com/"

response = requests.get(url)

print(response.status_code)
print(response.text)

