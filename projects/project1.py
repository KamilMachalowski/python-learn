import random

value1 = int(input("Enter the lower bound: "))
value2 = int(input("Enter the upper bound: "))

print(random.randrange(value1, value2 + 1, 1))