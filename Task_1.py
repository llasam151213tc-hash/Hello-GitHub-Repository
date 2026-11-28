menu = {
    "Burger": 85,
    "Fries": 45,
    "Drink": 30,
    "Chicken": 120
}

orders = {}

print("===== CANTEEN MENU =====")

for item, price in menu.items():
    print(item, "-", price)

number = int(input("\nEnter number of order attempts: "))

for i in range(1, number + 1): #Change range(1, number) to range(1, number +1),to include the total number of attemps.

    print("\nOrder", i)

    item = input("Enter item name: ").title()

    if item not in menu: #Changed "in" to "not in" to check if the item is NOT available in the menu.
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0: #Changed < 0 to <= 0 to prevent zero and negative quantities.
        print("Invalid quantity!")
        continue

    orders[item] = quantity

print("\n===== ORDER SUMMARY =====")

for item, quantity in orders.items():
    print(item, "x", quantity)
