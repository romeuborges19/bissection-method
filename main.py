from classes import BissectionMethod
import time

function = input("Please, insert a function: ")
print("Please, insert a interval [a, b]:")
a = int(input("- a: "))
b = int(input("- b: "))
stop = int(input("Insert an 'n' for 10**(-n): "))

print(f"Interval: [{a}, {b}] | Stop parameter: 10**(-{stop})")

obj = BissectionMethod(function)
result, root = obj.bissect(a, b, stop)
obj.printTable()
print(f"The {root} is x={result}")
obj.plotGraph(a, b)
