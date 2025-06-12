menu= {
    'pizza':40, 'pasta' :50, 'burger' :60, 'salad' :70, 'coffee' :80
}

print("Welcome to AT Restaurant")
print("Menu for you: Pizza: Rs40 \nPasta: Rs50 \nBurger: Rs60 \nSalad: Rs70 \nCoffee: Rs80")

Order_total= 0

item_1 = input(str.lower("what would you like to order: "))
if item_1 in menu:
    Order_total += menu[item_1]
    print(item_1, "is added")
else:
    print("Item not available")

next_item = input(str.lower("would you like to add anything else? (Yes/No)"))
if next_item == "yes":
    next_item = input(str.lower("Enter the next item: "))
    if next_item in menu:
        Order_total += menu[next_item]
        print(next_item ,"is added")
    else:
        print("Item not available")

print("your total is: ", Order_total)