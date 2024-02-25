import math
import cmath

print()
greetings = """
Hello, this is a program that will solve the quadratic formula for you.
Below type in the inputs for a, b and c.
"""
print(greetings)
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

#Starting Formula
d = -1 * b
e = (b ** 2) - (4 * a * c)
f = 2 * a 

#Deciding if the square root will be negative or positive
if e < 0:
    negative_e = cmath.sqrt(e)
    x_plus = (d / f) + (negative_e / f)
    x_minus = (d / f) - (negative_e / f)
    rounded_x_plus = "{:.5f}".format(x_plus)
    rounded_x_minus = "{:.5f}".format(x_minus)
else:
    positive_e = math.sqrt(e)
    x_plus = (d / f) + (positive_e / f)
    x_minus = (d / f) - (positive_e / f)
    rounded_x_plus = "{:.4f}".format(x_plus)
    rounded_x_minus = "{:.4f}".format(x_minus)

print()
print(f"x = {rounded_x_plus}\nx = {rounded_x_minus}")
print()