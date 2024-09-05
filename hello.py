# Program to add two numbers with error handling

try:
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Add the two numbers
    sum = num1 + num2

    text1 = 4
    dtype = "String" if isinstance(text1, str) else "Not String"
    print(dtype)

    # Display the result
    print("num1 is datatype: "+ str(type(num1)))
    print("num2 = "+ str(num2))
    print("The sum of {0} and {1} is {2}".format(num1, num2, sum))

except ValueError:
    # Handle the error if the user inputs a non-numeric value
    print("Invalid input. Please enter numeric values only.")
