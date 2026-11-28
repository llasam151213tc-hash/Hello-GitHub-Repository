#The canteen needs a billing system that calculates 
#the total cost of purchased items, applies discounts, 
#and determines the customer's change. Use the given dictionary

menu = {
    "Burger": 85,
    "Fries": 45,
    "Drink": 30,
    "Chicken": 120
}

orders = {
    "Burger": 3,
    "Fries": 3,
    "Chicken": 1,
    "Drink": 2
}
print("====CANTEEN MENU====")

for item, price in menu.items():
    print(item, "-", price)

print("\n====ORDER SUMMARY====")
total= 0

for item, quantity in orders.items():
    price = menu[item]
    subtotal = price * quantity

print(item, "x", quantity, "=", subtotal)
total += subtotal

print("\nTotal Amount:", total)

if total >= 500:
    discount = total * 0.10
    print("Discount (10%):", discount)
else:
    discount = 0
    print("Discount: 0")

final_amount = total - discount

print("Final Amount:" , final_amount)

payment = float(input("\nEnter payment amount:"))

if payment >= final_amount:
    change= payment - final_amount

    print("\n====CUSTOMER RECEIPT====")
    print("Total Amount:", total)
    print("Discount:", discount)
    print("Amount to Pay:", final_amount)
    print("Payment:", payment)
    print("Change:", change)
else:
    print("Insufficient payment!")
    print("You still need:", final_amount - payment)















    
