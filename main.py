#task 1 (variant A)
Customer_name = input( "Enter your name: " )
Product_name = input( "Enter product name : " )
Price_penu_KZ= float(input( "Enter price per unit (KZT): " ))
Quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))
f_total = 0

# task 2
subtotal = Price_penu_KZ * Quantity


if subtotal > 5000:
    f_total = subtotal * 0.90
    discount = subtotal  * 0.10
else:
    print( subtotal)

print ("=" *30 )
print( "SHOP RECEIPT")
print ( "=" * 30  )
print ( "customer : " + Customer_name )
print ( f"product : " + Product_name )
print ( f"quantity : " + str(Quantity) )
print( "-" *30)
print( "subtotal : " + str(subtotal) )
print( "discount : " + str(discount) )
print("total = " + str(f_total) )
print ("=" * 30 )

print("")
print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", f_total > 3000)


