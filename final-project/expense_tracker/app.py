# Main entrypoint of app Expense tracker


# Import Python libraries

# Imports local modules
from logic import get_all_expenses, add_expenses, validate, filter_by_month


def main_loop():
    """Interactive loop for managing expenses. Can later be replaced by GUI calls."""
    while True:
        # Menu
        print("\n1) Pievienot izdevumu")
        print("2) Parādīt izdevumus")
        print("7) Iziet")

        try:
            choice = int(input("Izvēlies: "))
        except ValueError:
            print("⚠ Lūdzu ievadi skaitli!")
            continue

        if choice == 1:
            try:
                expense = {
                    "date": validate("date"),
                    "category": validate("category"),
                    "amount": validate("amount"),
                    "docID": validate("docID"),
                    "description": validate("description"),
                    "paymentMeth": validate("paymentMeth")
                }
                
                if add_expenses(expense):
                    print(f"✓ Pievienots: {expense['date']} | {expense['category']} | {expense['amount']:.2f} EUR | {expense['docID']} | {expense['description']} | {expense['paymentMeth']}")
                else:
                    print("⚠ Kļūda pievienojot izdevumu!")
            except ValueError as e:
                print(f"⚠ {e}")

        elif choice == 2:
            lines = get_all_expenses()
            for line in lines:
                print(line)

        elif choice == 7:
            print("Paldies, uz redzēšanos!")
            break

        else:
            print("⚠ Nezināma izvēle.")


if __name__ == "__main__":
    main_loop()
   



