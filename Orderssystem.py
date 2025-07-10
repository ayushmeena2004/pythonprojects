#menu
#order placed
#amount
mydict = {
    "Pizza": 200, "Burger": 80, "Maggie": 40,
    "Manchuriyan": 40, "Coffee": 40, "ColdCoffee": 80,
    "Tea": 40, "Sandwich": 100, "Waterbottle": 20
}

i = True
while i:
    print("Select your Order")
    for key, value in mydict.items():
        print(f"{key}: {value}")

    item1 = input("Enter your order: ")
    bill = 0

    if item1 in mydict:
        print(f"You ordered {item1}")
        bill += mydict[item1]
    else:
        print("Sorry, this dish is not available\nThank You")
        continue  # If the dish is not available, restart the loop

    while True:  # Loop to allow multiple orders
        check = input("Do you want to order more? {Yes/No}: ")
        if check.lower() == "yes":
            item2 = input("Enter your order: ")
            if item2 in mydict:
                print(f"You ordered: {item1} and {item2}")
                bill += mydict[item2]
                print(f"Your bill is = {bill}")
            else:
                print("Sorry, this dish is not available")
        elif check.lower() == "no":
            print(f"Your total bill is = {bill}")
            i = False  # Exit the main loop
            break  # Exit the ordering loop
        else:
            print("Invalid input. Please enter Yes or No.")


