# ------------------- Activity 1-------------------------------

print("     |     |     ")
print("     |     |     ")
print("     |     |     ")
print("-----------------")
print("     |     |     ")
print("     |     |     ")
print("     |     |     ")
print("-----------------")
print("     |     |     ")
print("     |     |     ")
print("     |     |     ")

print("""
This
is
over
many
lines""")

# ------------------- Activity 2-------------------------------

print("the quick brown fox".upper()) 
#upper() makes all lowercase characters uppercase within the specified string. It does not need arguments 

print("THE QUICK brown fox".lower()) 
#lower() makes all uppercase characters lowercase within the specified string. It does not need arguments 

print("the quick bROWn fox.".capitalize()) 
#capitalize() will capitalise the first letter of the string, and make any other character lowercase. 
# It only works per string, sentences mean nothing. 


print("the quick brown fox fox fox".count("fox")) 
#count needs one argument. It counts all instances of the argument, and displays the amount in the terminal. This example would return "3". 

print("the quick brown foxfoxfox".count("fox")) 
#this example would still return 3, because our parameter is the word fox with no spaces either side 

print("the quick brown fox fox fox".count("fox ")) 
#this example would return 2, because our argument has a space at the end, and only two examples of the word fox do 

print("the quick brown fox fox fox".count("Fox ")) 
#this example would return 0. There are no instances of fox with a capital F in our string. The substrings are EXACT MATCHES 

print("the quick brown fox".find("quick")) 
#find() will give the index value of the first occurrence of the specified term in a string. 
# Here, it will show us the index of the start of quick, which is q. Because it is index, it starts the count from 0. 
# The output is 4, even though q is the 5th character.  

print("the quick brown fox".replace("fox","frog")) 
#replace() will replace a term with another term in a specified string. This will output as "the quick brown frog". 
# It needs two arguments to work as intended 

print("the quick brown fox ".strip()) 
#strip() removes characters from the beginning or the end of a string - depending on the argument. If no character is specified, it will remove spaces 

print("the quick brown fox".strip("the")) 
#strip() would remove the word "the" 

print("the quick brown fox".strip("brown")) 
#strip() would not remove anything - it only looks at the start and the end 

print("the quick brown fox".strip("the quick" "fox")) 
#use can use multiple strings if they target the start and the end 