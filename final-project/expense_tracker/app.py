# Main entrypoint of app Expense tracker

# Imports local modules
from logic import load_expenses, get_all_expenses, add_expenses, validate, filter_by_month, sum_by_categories, get_available_months, display_all_with_ids, delete_expense
from export import export_list

def header():
    '''Āpplication header'''
    print('''
.######..##..##..#####...######..##..##...####...######..........######..#####....####....####...##..##..######..#####..
.##.......####...##..##..##......###.##..##......##................##....##..##..##..##..##..##..##.##...##......##..##.
.####......##....#####...####....##.###...####...####..............##....#####...######..##......####....####....#####..
.##.......####...##......##......##..##......##..##................##....##..##..##..##..##..##..##.##...##......##..##.
.######..##..##..##......######..##..##...####...######............##....##..##..##..##...####...##..##..######..##..##.
........................................................................................................................
          ''')
def main_loop():
    '''Interactive loop for managing expenses. Can later be replaced by GUI calls.'''
    header()
    while True:
        # Menu
        print("\n" + "="*50)
        print("IZDEVUMU PĀRVALDNIEKS")
        print("="*50)
        print("1) Pievienot izdevumu")
        print("2) Parādīt izdevumus")
        print("3) Filtrēt pēc mēneša")
        print("4) Kopsavilkums pa kategorijām")
        print("5) Dzēst izdevumu")
        print("6) Eksportēt CSV/TXT")
        print("7) Iziet")
        print("="*50)

        try:
            choice = int(input("Izvēlies: "))
        except ValueError:
            print("⚠ Lūdzu ievadi skaitli!")
            continue

        if choice == 1:
            '''Izvēle - Pievienot izdevumu'''
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
            '''Izvēle - Parādīt izdevumus'''
            lines = get_all_expenses()
            for line in lines:
                print(line)
        
        elif choice == 3:
            '''Izvēle - Filtrēt pēc mēnešiem'''
            months = get_available_months()
            if not months: 
                print("Nav saglabātu izdevumu.")
            else:
                print("\nPieejamie mēneši")
                for idx, (month, count) in enumerate(months, start=1):
                    print(f"{idx}. {month} ({count} izdevumi)")
            
            while True:
                try:
                    month_choice = int(input("\nIzvēlies mēnesi (numurs): ").strip())
                    selected_month = months[month_choice - 1][0]
                    lines = filter_by_month(selected_month)
                    print(lines)
                    break

                except (ValueError, IndexError):
                    print("Nepareiza izvele")
        elif choice == 4:
            '''Izvēle - Kopsavilkums pa kategorijām'''
            print(sum_by_categories())

        elif choice == 5:
            '''Izvēle - Dzēst izdevumu'''
            expenses = load_expenses()
            if not expenses:
                print("⚠ Nav izdevumu dzēšanai.")
            else:
                print(display_all_with_ids())

                while True:
                    try:
                        idToDelete = int(input("Ievadi ID dzēšanai (vai 0 lai atceltu): ").strip())

                        if idToDelete == 0:
                            print("Atcelts.")
                            break

                        if not any(item.get("id") == idToDelete for item in expenses):
                            print(f"⚠ ID {idToDelete} nav atrasts.")
                            continue

                        confirm = input(f"Vai tiešām vēlaties dzēst ID {idToDelete}? (jā/nē): ").lower()

                        if confirm in ["jā", "ja"]:
                            if delete_expense(idToDelete):
                                print(f"✓ ID {idToDelete} veiksmīgi dzēsts")
                            else:
                                print("⚠ Kļūda saglabājot datus.")
                            break
                        else:
                            print("Dzēšana atcelta.")
                            break

                    except ValueError:
                        print("⚠ Lūdzu ievadi skaitli!")
        elif choice == 6:
            '''Izvēle - Eksports CSV/TXT'''
            expenses = load_expenses()
            if not expenses:
                 print("⚠ Nav datu eksportēšanai.")
                 return
            filename = input("Ievadi faila nosaukumu [Noklusējumā: izdevumi.csv]: ").strip()
            file_type = input("Ievadi faila veidu CSV vai TXT: ").strip().lower()

            if file_type not in ["csv", "txt"]:
                print("Nekorekts faila formāta veids - ievadiet CSV vai TXT")

            if not filename:
                filename = "izdevumi"
            
            try:
                if export_list(file_type=file_type, filename=filename):
                    print(f"✓ Eksports veiksmīgs.")
                else:
                    print("⚠ Eksports neizdevās.")
            
            except ValueError:
                print("⚠ Atbalstītie formāti: .csv vai .txt")

        elif choice == 7:
            '''Izvēle - Iziet'''
            print("\nPaldies, uz redzēšanos!")
            break

        else:
            print("⚠ Nezināma izvēle.")


if __name__ == "__main__":
    main_loop()
   



