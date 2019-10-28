import random

side1: int = random.randint(1, 100)
side2: int = random.randint(1, 100)
side3: int = random.randint(1, 100)

if side1 == side2 or side1 == side3 or side2 == side3:
    print(side1)
    print(side2)
    print(side3)
    print("You can create an isosceles triangle with the current side sizes")

if side3 == side2 == side1:
    print(side1)
    print(side2)
    print(side3)
    print("You can create an equatorial triangle")

if side1 != side2 and side1 != side3 and side2 != side3:
    print(side1)
    print(side2)
    print(side3)
    print("You have a random triangle")
