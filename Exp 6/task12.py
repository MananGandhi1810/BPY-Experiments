from interest import compound, simple

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

print(f"The simple interest is: {simple.simple_interest(principal, rate, time)}")
print(f"The compound interest is: {compound.compound_interest(principal, rate, time)}")