# music = input("What music would you like?").lower()

# if music == "classical":
#     print("Oh no, not classical again!")
# elif music == "no music":
#     print("Alexa, play some music!")
# elif music == "britpop":
#     print("My second favourite! Turn it up!")
# else:
#     print("I've not heard this before!")

# music = "britpop"

# if music == "Oasis":
#     print("The best!")
# elif music !="britpop":
#     print("I want to listen to britpop")
# else:
#     print("Yay! Britpop!")

# place = "MCR"
# weather = "Cloudy"
# if place == "MCR" and weather == "Sunny":
#     print("Check again!")
# elif place =="MCR" and weather == "Rain":
#     print("Obvs")
# else:
#     print("What? It isn't raining?")

# day = "Monday"
# bank_holiday = True

# if day == "Saturday" or day == "Sunday" or bank_holiday==True:
#     print("A day off!")
# else:
#     print("Off to work I go.")

password = input("Enter your password: ")
p_len = len(password)
# print(p_len)
if p_len <= 8:
    print("The password is too short")
else:
    print(password)