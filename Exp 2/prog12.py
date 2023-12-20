"""
Write a program to print the following pattern:
5 4 3 2 1
  4 3 2 1
    3 2 1
      2 1
        1
"""

for i in range(5,0,-1):
    for j in range(5-i):
        print("  ", end="")
    for j in range(i,0,-1):
        print(j, end=" ")
    print()