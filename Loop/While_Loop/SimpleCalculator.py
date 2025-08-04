while True:
    choice = input("Enter +, -, *, / or q to quit: ")
    if choice == 'q':
        break
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == '+':
        print(a + b)
    elif choice == '-':
        print(a - b)
    elif choice == '*':
        print(a * b)
    elif choice == '/':
        print(a / b)
    else:
        print("Invalid choice")
