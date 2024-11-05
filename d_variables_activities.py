
# ?input takes answer from a user
# ?.capitalize() makes the first letter a capital, ensuring my data comes in as expected
my_name = input("What is your name?").capitalize()
age = int(input("What is your age?"))
favourite_colour = input("What is your favourite colour?").lower()

print(f"Hello my name is {my_name}, I am {age} years old. My favourite colour is {favourite_colour}.")

# ! ---------- Activity 2 --------------------

num1 = int(input("Type in a first number: "))
num2 = int(input("Type in a second number: "))

add_result = num1+num2
print(f"{num1} + {num2} = {add_result}")

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} ** {num2} = {num1**num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} % {num2} = {num1%num2}")

apple_cost = 25
apple_amount = int(input("How many apples would you like to buy?"))

apple_total = apple_cost * apple_amount

banana_cost = 50
banana_amount = int(input("How many bananas would you like to buy?"))

banana_total = banana_cost * banana_amount

total = apple_total + banana_total

print(f"You bought {apple_amount} apples")

print(f"You bought {banana_amount} bananas")

print(f"Your total is {total}p")
print(f"Your total is £{total/100:.2f}")
