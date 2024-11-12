
#* ------------------- Random Number Generator ------------------

#? Import the random module to generate random numbers
import random 

#? "Pseudo code" - code-ish 

# I have a number
# computer picks random number
# computers checks mine and its number
# while numbers don't match 
#  - computer picks new number
# if numbers match, computer wins 

#? Setting my number to 13
my_number = 13 

#? Generate the computer's initial random number between 1 and 50
computer_number = random.randint(1,50)

#? Loop until the computer's number matches the player's number
while my_number != computer_number:
    #? If numbers don't match, print the current numbers and indicate no match
    print(f"Computer picked {computer_number}. You picked {my_number}. These don't match")
    #? Generate a new random number so the condition has a chance to change
    computer_number = random.randint(1,50)
#? This `else` block executes when the `while` loop condition is no longer true
#? (i.e., when my_number == computer_number)
else:    
    print(f"Computer picked {computer_number}. You picked {my_number}. These do match! Well done computer!")