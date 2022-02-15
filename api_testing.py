import requests
r = requests.get("https://breakfastapi.fun/")
data = r.json()

print(data["recipe"]["ingredients"])
print(data["recipe"]["directions"])