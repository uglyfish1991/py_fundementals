
#? -------------- Pizza Machine --------------------------

#? This is not the most effective way of doing this, but this code will continue to allow me to make orders until I "turn the machine off"

order_count = 0

def take_order(topping, size, style):
    global order_count
    print("{}inch {} pizza with {}".format(size, style, topping))
    order_count +=1
    print(f"Your order is order number : {order_count}")
    print()

#? While True loops ALWAYS run, and carry on running until they encounter the break keyword
while True:
    #? first job of the loop is to run the function
    take_order(input("Enter your pizza topping:  > "),input("Enter your pizza size:  > "),input("Enter your pizza style:  > "))
    #? The function runs and then comes back here into the loop
    continue_question = input("Would you like to switch the machine off? Please type yes or no").lower()
    #? The while loop makes sure the user can only type in "yes" or "no"
    while continue_question !="yes" and continue_question !="no":
        print("Please only type yes or no")
        continue_question = input("Would you like to switch the machine off? Please type yes or no").lower()
    else:
        if continue_question == "no":
            continue
        else:
            #? The break keyword stops this, and all future itteration of the loop, turning the machine "off"
            break