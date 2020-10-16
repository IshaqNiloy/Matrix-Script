#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
string = ''

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)



for col in range(m):
    for row in range(n):
        string += matrix[row][col]#To convert the list into a single string 

print(re.sub(r'\b[^A-Za-z0-9]+\b',' ', string))#Finds a group of non alphanumeric characters and replaces it with a space
