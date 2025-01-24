# Aim: Write a Program to make simple calculator using if statements
# Branch: COMPS
# Year: 2nd
# Sem: 4
# Subject:Python lab
# Name: Pathan Mugaira Zakeer
# UIN:231P084
# Roll No.:25

print("***************************")
print("Simple Calculator")
print("Pathan Mugaira")
print("***************************")
print("*****MENU*****")
print("\nMENU")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Exit")

while True:
    choice = int(input("Enter operation: "))
    
    if choice >= 1 and choice <= 5:
        print("Enter two numbers:")
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        
        if choice == 1:
            res = num1 + num2
            print("Result: ", res)
        elif choice == 2:
            res = num1 - num2
            print("Result: ", res)
        elif choice == 3:
            res = num1 * num2
            print("Result: ", res)
        elif choice == 4:
            if num2 != 0:
                res = num1 / num2
                print("Result: ", res)
            else:
                print("Error! Division by zero.")
        elif choice == 5:
            res = num1 % num2
            print("Result: ", res)
    elif choice == 6:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Wrong input..!! Please enter a valid choice.")
