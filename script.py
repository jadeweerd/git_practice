import requests

r = requests.get("https://www.delagewaard.nl")
print(r.status_code)
print(r.ok)
