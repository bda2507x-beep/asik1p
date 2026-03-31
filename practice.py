Customer_name = input("Enter your name: ")

subtotal = 0
t_item = 0
discount = 0
f_total = 0

while True:
    item = input("Enter product: ")
    if item.strip().lower() == "done":
        break
    i_price = float(input("Enter price: "))
    subtotal += i_price
    t_item += 1

if subtotal < 3000:
    discount = 0
elif subtotal < 7000:
    discount = subtotal * 0.05
else:
    discount = subtotal * 0.15

f_total = subtotal - discount

print("=" * 30)
print("SHOP RECEIPT")
print("=" * 30)
print("customer :", Customer_name.upper())
print("items :", t_item)
print("-" * 30)
print("subtotal :", subtotal)
print("discount :", discount)
print("total =", f_total)
print("=" * 30)

print("")
print("Discount applied:", discount > 0)
print("Paid more than 3000:", f_total > 3000)