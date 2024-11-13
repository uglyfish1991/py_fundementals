
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


#* ------ Oother Comparison Operators ------------

#? There are other comparison operators that exist. These are: 
#? == equal to
#? != not equal to
#? > less than
#? < greater than
#? >= less than or equal to
#? <= greater than or equal to

music = "britpop"

#? Here, we are saying "if music does not equal britpop" - this will be the case for anything but britpop!
if music !="britpop":
    print("I want to listen to britpop")
else:
    print("Yay! Britpop!")

#------------------------------------------------

#? An if statement will do the first true thing it encounters - even if there is something more true further down. Take this code for example:
#? Even though Oasis is there, we will see "I want to listen to britpop"
#? This is because the first check is music != "britpop"
#? The string Oasis does not match the string britop. It is true to say they don't match - and so we see "I want to listen to britpop"
music = "Oasis"

if music !="britpop":
    print("I want to listen to britpop")
elif music == "Oasis":
    print("The best!")
else:
    print("Yay! Britpop!")

#? When ordering an if statement, there are many approaches, but usually the most specific thing comes first! 

if music == "Oasis":
    print("The best!")
elif music !="britpop":
    print("I want to listen to britpop")
else:
    print("Yay! Britpop!")

#* ------ Logical Operators ------------

#? We can use logical operators to expand our if statements, and look at multiple conditions.
#? These logical operators are very like English. They are words like "and", "or"!

#? Here, both conditions need to match. We would need to see MCR AND Sunny to get the response "Check Again!"

place = "MCR"
weather = "Cloudy"
if place == "MCR" and weather == "Sunny":
    print("Check again!")
elif place =="MCR" and weather == "Rain":
    print("Obvs")
else:
    print("What? It isn't raining?")

#? We can use or to have many comparisons trigger the same response. If its Saturday, Sunday, or a Bank Holiday, any of them will trigger the response "A day off!"
#? This saves me having to write many elifs which do the same thing!

day = "Monday"
bank_holiday = True

if day == "Saturday" or day == "Sunday" or bank_holiday==True:
    print("A day off!")
else:
    print("Off to work I go.")

