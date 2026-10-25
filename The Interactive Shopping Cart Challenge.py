import time

print()
print("Welcome to \033[1mPython Supermarket\033[0m!")
# \033[7m highlights the word, \033[0m resets it
print("Where shopping always \033[7mimport\033[0ms happiness!")
print()
name = input("Enter your name please: ")
print()

cart = []
current_time = time.localtime()
time = time.strftime("%B %d, %Y, %A || %I:%M:%S %p", current_time)
#print(time)
program_open = True
while program_open:
    print("1- Add Item")
    print("2- Remove Item")
    print("3- View Cart")
    print("4- Checkout & Exit")
    choice = input("Enter your choice (1, 2, 3 or 4): ")
    if choice == "1":
        item_name = input("Enter item name: ")
        cart.append(item_name)
        print("Item added to cart!")
        print()
    elif choice == "2":
        item_name = input("Enter item name: ")
        if item_name in cart:
            cart.remove(item_name)
            print("Item removed from cart!")
            print()
        else:
            print("Item not found in cart!")
            print()
    elif choice == "3":
        if len(cart) == 0:
            print("No items found!")
            print()
        else:
            print("Your Cart: " + str(cart))
            print()
    elif choice == "4":
        print()
        print("\033[1mPython Supermarket\033[0m")
        print(name)
        print(time)
        print()
        print(cart)
        print()
        print("Thank you for shopping!")
        print("Python Supermarket: Where your cart never returns \033[7mNone\033[0m")
        program_open = False

        receipt = str(cart)
        # Record data
        with open("The Interactive Shopping Cart Challenge Data.txt", "a") as file:  # "a" is used for append
            file.write(
                "Name: " + name + " || " + time + " || " + "Cart: " + receipt + "\n")  # "/n" is used to add a separate line