#!/usr/bin/python3
/* a program that imports the function def add(a, b): from
the file add_0.py and prints the result of the addition 1 + 2 = 3
*/
a = 1, b = 2

from add_0 import add

result = add(a, b)
print("{} + {} = {}")
