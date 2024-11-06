# -------------------- Data, Properties, and Methods -------------------------

# The print() function is how I can see things in the terminal
print("This sentence will output into my terminal")

# The different data types within programming help the language know what can and can't be done to a piece of data. We know we can't spellcheck numbers, or add words up. The data type helps influence that. 

# Python has many data types, but the simple types are:

# #This is a string - a collection of characters all strung together!
print("A string is a collection of characters")
print("Strings are surrounded by speech marks")
print("1234")
print("Even that is a string! It is not the number 1234, we couldn't do maths with it")
print("12 + 34")

# # Integers are whole numbers. They have mathematic values, I can use operators on them
print(1234)

# I'll type 12 + 34, but the terminal will output 46, because these data points can be used mathematically
print(12 + 34)

# # Floating points are fractional numbers
print(12.34)

# # None is blank data
print(None)

# #Boolean - True or False, yes or no, on or off. One or the other.
print(True)
print(False)

# ------------------ Properties -----------------------

# As objects, the data types have information about their contents. These are called properties. We can find out a property of a string - its length

print(len("hello world"))

# This tells us how many characters long the string is.
# It can be useful to know how long a string is - examples include password length, phone number length (phone numbers are often saved as strings because we don't need to do maths on them) etc

# We can use index position to pinpoint a particular character in the string 
# When we use index, we need to remember that it starts at 0 
print("hello"[0]) 
#will show "h" - even through WE see it as the first character, in this case it has an index of 0 

print("hello"[1]) 
print("hello"[2]) 
print("hello"[3]) 
print("hello"[4]) 

# on other objects, we might access properties using something called dot notation. This is written as:

# object.method()
# thing we want to work on. thing we want to do()
# string.stringmethod()

# One example is .upper - this works on a string to change it to uppercase.
print("hello world".upper())

# These methods are useful to manipulate strings that we might not have access to yet. These could be applied to user input to ensure data is coming in at the quality we expect



