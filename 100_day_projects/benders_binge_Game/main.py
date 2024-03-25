from art import *

width = 10
height = 10

matrix = [["_" for x in range(width)] for y in range(height)]
matrix[0][0] = bender

print()
print(*matrix, sep = "\n")
print()

