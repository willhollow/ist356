# Let's write a program to divide up the check among diners in a party.

def main():
    try:
        check_amount = float(input("Enter the amount of the restaurant check: "))
        if check_amount < 0:
            print("The check amount cannot be negative.")
            return

        tip_percentage = float(input("Enter the tip percentage: "))
        if tip_percentage < 0:
            print("The tip percentage cannot be negative.")
            return

        number_of_diners = int(input("Enter the number of diners: "))
        if number_of_diners <= 0:
            print("The number of diners must be greater than zero.")
            return

        total_amount = check_amount + (check_amount * tip_percentage / 100)
        amount_per_diner = total_amount / number_of_diners

        print(f"Total amount with tip: ${total_amount:.2f}")
        print(f"Amount each diner owes: ${amount_per_diner:.2f}")

    except ValueError:
        print("Please enter numbers only.")


main()

