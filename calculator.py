def add(num1,num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 ==0:
        return "Error: Can't divide by zero"
    else:
        return num1/num2
    
    def calculator():
        print("Select an operation:")
        print("1.Add")
        print("2.Subtract")
        print("4.Divide")

        choice = input("Enter choice(1/2/3/4):")

        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == "1":
            print(add(num1,num2))
        elif choice =="2":
            print(subtract(num1,num2))
        elif choice == "3":
            print(multiply(num1,num2))
        elif choice =="4":
            print(divide(num1,num2))
        else:
            print("Invalid choice. Please enter a valid option.")


    