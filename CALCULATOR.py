# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiplication(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function
def main():
    while True:
        # Display menu
        print("Options:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        


        # Get user choice
        choice = input(" Enter your choice (1/2/3/4): ")
        
        # Get user input for numbers
        if choice in ("1","2","3","4","5"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        
        
            if choice == "1":
                result = add(num1, num2)
                print("Result: ", result)
            elif choice == "2":
                result = subtract(num1, num2)
                print("Result: ", result)
            elif choice == "3":
                result = multiplication(num1, num2)
                print("Result: ", result)
            elif choice == "4":
                result = divide(num1, num2)
                print("Result: ", result)

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


            
        
                
