""""Basic Calculator Program"""

import os

def main():
    print("\t\t\t*** Basic Calculator ***\t\t\t")

    print("Enter two values:")
    value1 = float(input("Enter Value 1: ")) #type casting user input
    value2 = float(input("Enter Value 2: "))

    os.system('clear')
    print("Choose an operation: (use numbers)")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    choice = int(input()) #choice of operation

    #switch statement 
    match choice:
        case 1: print(f"{value1} + {value2} = {value1 + value2}")
        case 2: print(f"{value1} - {value2} = {value1 - value2}")
        case 3: print(f"{value1} * {value2} = {value1 * value2}")
        case 4: print(f"{value1} / {value2} = {value1 / value2}")

main()
                

