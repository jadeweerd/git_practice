import sys
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Corey'))

r = requests.get("https://www.delagewaard.nl")
print(r.status_code)
