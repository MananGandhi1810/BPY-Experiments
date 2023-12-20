"""
Write a program to accept the cost price of a bike and display the road tax to be paid according to following criteria:
>100000 -> 15%
>50000 and <=100000 -> 10%
<=50000 -> 5%
"""

cost_price = float(input("Enter the cost price of the bike: "))

if(cost_price>100000):
    print(f"Road tax to be paid is 15% = {cost_price*0.15}")
elif(cost_price>50000):
    print(f"Road tax to be paid is 10% = {cost_price*0.1}")
else:
    print(f"Road tax to be paid is 5% = {cost_price*0.05}")