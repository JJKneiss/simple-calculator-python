while True:
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))
        if operator == "+":
            print("Result:", first_number + second_number)
        elif operator == "-":
            print("Result:", first_number - second_number)
        elif operator == "*":
            print("Result:", first_number * second_number)
        elif operator == "/":
            if second_number == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", first_number / second_number)
        else:
            raise ValueError()
            # print("Invalid operator. Please enter a valid operator (+, -, *, /).")
        break
    except ValueError:
        print("Invalid input. Please try again.")
        continue
