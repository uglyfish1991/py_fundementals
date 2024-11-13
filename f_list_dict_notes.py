
#* ------------------ Lists -----------------------

#? Lists allow us to store many elements with a similar thing in one place. This is very reflective of real life. 
#? A task list, shopping list, or wishlist are all single structures that hold different pieces of information but with a running theme!
#? Let's look at taking a coffee order

#? Python lists are stored within [] brackets 
#? Elements with the list are split by commas , apart from the last item, which isn't being split from anything!
#? To refer to the list easier, I've assigned it to the variable coffee_order

coffee_order = [
    "Alex - Cortado", 
    "Ben - Latte",    
    "Charlie - Mocha"
]

#? A list is a container data type. I can access the whole collection by using the variable name:
print(coffee_order)

#? Or I can access individual elements within the list using index position
#? Remember, index position starts at 0 - index position 2 will give us back Charlie - Mocha
print(coffee_order[2])

#? I can use that index position to assign a new value to that element, just as I would update any other variable!
coffee_order[2] = "Charlie - Hot Chocolate"
#? Charlie now wants a hot chocolate!
print(coffee_order[2])

#? We can also find out properties of our list using the len() function, to return the length of the list.
print(len(coffee_order))

#? Because lists are a built in data type, they have built in methods which we can use to work with our lists dynamically. They are accessed via dot notation:
#* object.method()
#* list.listmethod()

#? These methods have specific jobs. .append() adds a new item to the end of the list
coffee_order.append("Diane - Cappuccino")
print(coffee_order)

#? .pop() removes the last item from a list, or an element at a specific index position 
# coffee_order.pop(1)
# print(coffee_order)

#* ---------------- Dictionaries ---------------------------

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
