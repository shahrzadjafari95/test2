class Calculator:
    def multiplication(self, *args):
        res = 1
        for i in args:
            res *= i

        return res




while True:
    print("Select operation:")
    print("1. Multiply")

    choice = input("Enter your choice (1-5): ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == "1":
            res = Calculator.multiplication(num1, num2)
            print("Result:", res)

    elif choice == "5":
        print("Exiting...")
        break
     elif choice == "6":
        print("Invalid choice. Please try again.")
     else:
        print("... for test")

    print()

