menu = {
    "pizza" : 40,
    "pasta" : 50,
    "Burger" : 60,
    "Salad" : 70,
    "Coffee" : 80,
    "Tea" : 30,
    "Sandwitch" : 40,
    "momos" : 20
}
print("Welcome to MARWADI Restaurent")
print(" pizza: Rs 40\n pasta :RS 50 \n Burger : RS 60\n Salad : Rs 70 \n Coffe : Rs 80 \n Tea : Rs 30 \n Sandwitch : Rs 40\n momos : Rs 20")



order_total = 0
# 80+20 = 100
item_1 = input("enter the name of item you want to order = ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else :
     print(f"Ordered item {item_1} is not available yet \nplease order something else we can serve you")


another_order = input("Do you want to add another item ? (yes/No) ")
if (another_order == "yes") :
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available \n please order something in menu list")

print(f"the total amount of items to pay is {order_total}")


