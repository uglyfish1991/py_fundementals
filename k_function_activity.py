# def birthday_song(name):
#     print(f"Happy Birthday to you,",
#          "Happy Birthday to you,",
#          f"Happy Birthday dear {name},",
#            "Happy Birthday to you")
    
# birthday_song(input("Who am I singing to?"))

order_count = 0



def take_order(topping, size, style):
    global order_count
    print("{}inch {} pizza with {}".format(size, style, topping))
    order_count +=1
    print(f"Your order is order number : {order_count}")
    print()
    

take_order("pineapple", "18", "deep pan")
take_order("cheese", "11", "deep pan")
take_order("veggie", "28", "deep pan")
 