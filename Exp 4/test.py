veg_menu = ["Veg Roll", "Noodles", "Fried Rice", "Manchurian", "Soup"]
non_veg_menu = ["Chicken Roll", "Noodles", "Fried Rice", "Chilli Chicken", "Soup"]

def order(preference, order_list):
    menu = []
    if preference == "veg":
        menu = veg_menu
    elif preference == "non-veg":
        menu = non_veg_menu
    else:
        print("Enter a valid preference")
        return
    for index, item in enumerate(menu):
        print(index+1, item)
    choice = int(input("Enter your choice: "))
    order_list.append(menu[choice-1])
    print("Your order is: ", order_list)
    for index, item in enumerate(order_list):
        print(index+1, item)
    want_more = input("Do you want to order more? (y/n): ")
    if want_more == "y":
        order(preference, order_list)
    else:
        print("Thank you for your order")
    
preference = input("Enter your preference (veg/non-veg): ")
order_list = []
order(preference, order_list)