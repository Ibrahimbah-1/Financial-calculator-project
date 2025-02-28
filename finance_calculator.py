def loan_payment():
    principal = float(input("Enter loan amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter loan term (years): "))

    monthly_rate = rate / 12 / 100
    months = years * 12
    payment = principal * monthly_rate

    print("Your estimated monthly payment is:", round(payment, 2))


def compound_interest():
    principal = float(input("Enter initial investment: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    amount = principal + (principal * rate * years / 100)

    print("Your future investment value is:", round(amount, 2))


def savings_growth():
    initial = float(input("Enter initial savings amount: "))
    monthly = float(input("Enter monthly contribution: "))
    years = int(input("Enter number of years: "))

    total = initial + (monthly * 12 * years)

    print("Your total savings after", years, "years is:", round(total, 2))


while True:
    print("\nSimple Financial Calculator")
    print("1. Loan Payment Calculator")
    print("2. Compound Interest Calculator")
    print("3. Savings Growth Calculator")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        loan_payment()
    elif choice == '2':
        compound_interest()
    elif choice == '3':
        savings_growth()
    elif choice == '4':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-4.")




