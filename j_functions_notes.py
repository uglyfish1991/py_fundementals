# def say_hello():
#     print("Hello!")

# say_hello()

# def say_goodbye():
#     print("Goodbye!")

# say_goodbye()

# def say_something(something):
#     print(f"{something}")

# say_something("Hello everyone!")
# say_something("This is a lesson on functions")

balance = 500


def cash_withdrawal(amount, accnum):
    global balance
    print(f"Your balance is currently: {balance}")
    print(f"You have withdrawn £{amount} from account:{accnum}")
    balance -=amount
    print(f"Your new balance is: {balance}")

cash_withdrawal(300,12345678)
cash_withdrawal(150,12345678)

