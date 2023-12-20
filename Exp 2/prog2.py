# Write a program to display “Hello” if a number entered by the user is a multiple of five, otherwise print “Bye”.

num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")
