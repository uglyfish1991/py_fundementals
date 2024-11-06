# coffee_order = [
#     "Alex - Cortado", 
#     "Ben - Latte",    
#     "Charlie - Mocha"
# ]

# # print(coffee_order[2])

# # coffee_order[2] = "Charlie - Hot Chocolate"

# # print(coffee_order[2])

# print(len(coffee_order))

# # object.method()
# # list.listmethod()

# coffee_order.append("Diane - Cappuccino")
# print(coffee_order)

# coffee_order.pop(1)
# print(coffee_order)

# capital_cities = {
#     "England":"London",
#     "Scotland" : "Edinburgh",
#     "Wales": "Cardiff",
#     "Northern Ireland" : "Belfast",
#     "Ireland": "Dublin"
# }

# print(capital_cities["Wales"])

animals = {
    "Lion" : "Cub",
    "Pigeon" : "Squab",
    "Gecko" : "Baby gecko",
    "Hedgehog" : "Hoglet"
}

animals["Gecko"] = "Hatchling"

print(animals)

print(animals.keys())
print(animals.values())
print(animals.items())

print(animals["Gecko"])
print(animals.get("Zebra", "The key could not be found!"))

animals.setdefault("Dog", "Puppy")
animals.setdefault("Lion", "Baby Lion")

print(animals)
