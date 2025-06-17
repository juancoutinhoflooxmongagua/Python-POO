import requests

url = "https://www.google.com.br/?hl=pt-BR"

response = requests.get(url)

print(response.text)
