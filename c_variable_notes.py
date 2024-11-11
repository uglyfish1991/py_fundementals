
# !-----------------Variables----------------

#? Variables are names or references we can use to refer to data that might change (vary), data that we don't have yet, or simply data that we will need to use a few times in our code. 

# ? This is the string Katy

"Katy"

#? But if I needed to use that information elsewhere, how could I reference it? I've no name to call it by!

my_name = "Katy"
print(my_name)
#? Assigning a variable name means I have a term I can use to refer to this data. It's a bit like a storage box. 
#? Variables can contain any data type:
my_age = 33
is_a_leaner = False
favourite_drink = "latte"

#? When using variables, it's not often we just need the information the variable stores. We mornally need that information and some context! If I print(favourite_drink)
print(favourite_drink)

#? "latte" will output to the terminal, but that doesn't really make sense on its own! We can use variables in strings for context.
#? There are four common ways to do this.

#? The first is using commas to give print many arguments. Here, we are asking print() to print two things - the string, and the variable
#? This is the oldest method, and works well
print("My favourite drink is", favourite_drink)

#? It can get a little complicated to write if we have more than one variable, though, and I'm not necessarily in control of where all the spaces go!
print(my_name, "'s favourite drink is", favourite_drink)

#? The second method is concatenation - joining strings together with the +
print("My favourite drink is " + favourite_drink)
print(my_name + "'s favourite drink is " + favourite_drink)

#! Concatentation cannot mix strings and numbers - the + sign has different uses depending on the data type!
#! print(my_name + "is" + my_age + "their favourite drink is " + favourite_drink)
#? Because my_age is an integer, the + sign tries to do maths, and we can't add a string to an int. This is a limitation of concatentaion

#? .format() is a string method. .format() takes the ability to mix data types from the first way, with the control over spaces from the second way, and puts them into one. 
#? .format() uses {} as placeholders in the string. In the method itself, we hand over the variables in the order we want them to appear. It is very useful output-wise but it did get a bit tough readability wise!
print("{} is {} years old, and their favourite drink is {}".format(my_name, my_age, favourite_drink))

#? The newest method is the f-string. The f-string works like .format(), using {} to make placeholders, but here, we fill the {} with the
#* expression we want evaluating
#? This is a fancy way of saying that the string will work out the {} first, and then put that intromation into the string
print(f"{my_name} is {my_age} years old, and their favourite drink is {favourite_drink}")

# # -------- Input Code -----------

# # user_name = input("Type your name here:  > ")

# # print(f"Hello, {user_name}")
# # print(type(user_name))

# # print(3+7)
# # print(7-4)
# # print(3*2)
# # print(3**3)
# # print(15/3)
# # print(16%3)

# # balance = 100
# # amount_to_withdraw = 20
# # print(balance)
# # balance = balance - amount_to_withdraw
# # # balance -=amount_to_withdraw
# # print(balance)

# print("Type in two numbers to multiply them")

# num1 = int(input("Type in your first number: "))
# num2 = int(input("Type in your second number: "))

# print(num1*num2)

my_fav_fruit,my_worst_fruit = "apples", "grapes"

print(my_worst_fruit)