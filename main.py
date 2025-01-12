""""Basic Calculator Program"""

import os

def main():
    while True:
        print("\t\t\t*** Basic Calculator ***\t\t\t")

        print("Enter two values:")
        value1 = input("Enter Value 1: ") #type casting user input

        try:    #check if value 1 is a number
            value1 = float(value1) #type cast from string to float
        except ValueError:
            print("Value is not a number")
        
        value2 = input("Enter Value 2: ")
        try:    #check if value 2 is anumber
            value2 = float(value2)
        except ValueError:
            print("Value is not a number")

        os.system('clear')
        print("Choose an operation: (use numbers)")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")

        choice = input() #choice of operation

        try: #check if choice is number
            choice = int(choice) #type cast from string to int
        except ValueError:
            print("value is not a number")

        #switch statement 
        match choice:
            case 1: print(f"{value1} + {value2} = {value1 + value2}")
            case 2: print(f"{value1} - {value2} = {value1 - value2}")
            case 3: print(f"{value1} * {value2} = {value1 * value2}")
            case 4:
                if value2 == 0:
                    print("Can't divide by 0")
                else: 
                    print(f"{value1} / {value2} = {value1 / value2}")
            case _: print("Invalid choice. Please enter values range 1 to 4")

        another = input("Do you want to perform another operation (yes/ no): ")
        if another.lower() != 'yes':
            break
        os.system('clear')

main()
                

