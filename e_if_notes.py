
#* If / Else

#? If Else allows us to write conditional code. So far, all the code we've written will run all the time unless it's commented out.
#? With if/else, certain bits of code need to meet a criteria to run, meaning we can write code with options / choices. 

#? = is an assignment operator, it assigns the thing on the right to the reference on the left
#? == is a comparison operator - it looks to see is the thing on the right the same as the thing on the left?

#? Type in a music genre below!
#? You'll see either True or False appear. 
#? The code music=="classical" is comparing the thing you typed in to the string "classical" and seeing if they are the same
music = input("What music would you like?").lower()
print(music=="classical")

#? With an if statement, we can start to write out conditions. We write them very closely to how we word them in English!
#? If this matches,
    #? do this

if music == "classical":
    print("Oh no, not classical again!")
elif music == "no music":
    print("Alexa, play some music!")
else:
    print("I've not heard this before! Turn it up!")


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