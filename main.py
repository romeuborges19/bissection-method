from classes import BissectionMethod
import time

def main():

    function = input("Please, insert a function: ")

    obj = BissectionMethod(function)

    while True:
        print("Please, insert a valid interval [a, b]:")
        a = int(input("- a: "))
        b = int(input("- b: "))
        if obj.f(a)*obj.f(b) < 0:
            break

    stop = int(input("Insert an 'n' for 10**(-n): "))


    print(f"Interval: [{a}, {b}] | Stop parameter: 10**(-{stop})")

    result, root = obj.bissect(a, b, stop)
    obj.printTable()
    print(f"The {root} is x={result}")
    obj.plotGraph(a, b)

if __name__=='__main__':
    main()
