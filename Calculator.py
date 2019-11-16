while True:
    print("Options:")
    print("Enter 'add' to add two numbers.")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers.")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'Quit' to exit")
    user_input = input(": ")

    if user_input == "quit":  # The quit option
        break  # break stops the program
    elif user_input == "add":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = str(num1 + num2)  # adds numbers together
        print("The answer is " + result)  # produces the output
        print("")
    elif user_input == "subtract":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = str(num1 - num2)  # subtracts numbers
        print("The answer is " + result)  # produces the output
        print("")
    elif user_input == "multiply":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = str(num1 * num2)  # multiplies numbers
        print("The answer is " + result)  # produces the output
        print("")
    elif user_input == "divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = str(num1 / num2)  # divides numbers
        print("The answer is " + result)  # produces the output
        print("")

    


