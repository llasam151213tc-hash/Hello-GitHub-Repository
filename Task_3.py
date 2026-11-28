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

for i in range(1, number + 1):

    print("\nOrder", i)

    item = input("Enter item name: ").title()

    if item not in menu:
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity!")
        continue

    orders[item] = orders.get(item, 0) + quantity

print("\n===== ORDER SUMMARY =====")

total = 0

for item, quantity in orders.items():
    subtotal = menu[item] * quantity
    print(item, "x", quantity, "=", subtotal)
    total += subtotal

if total >= 500:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("\nSubtotal: ₱", total)
print("Discount: ₱", discount)
print("Total Amount: ₱", final_amount)

if total > 0:

    payment = float(input("\nEnter payment amount: "))

    if payment >= final_amount:
        change = payment - final_amount

        print("\n===== PAYMENT RECEIPT =====")
        print("Total Amount: ₱", final_amount)
        print("Payment: ₱", payment)
        print("Change: ₱", change)

    else:
        balance = final_amount - payment

        print("Insufficient payment!")
        print("Remaining Balance: ₱", balance)

else:
    print("No valid orders found.")