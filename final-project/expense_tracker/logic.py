# Utility to handle bussiness logic and calculations
# Import standart libs
from decimal import Decimal, InvalidOperation
from datetime import datetime

# Import local modules
from storage import load_expenses, save_expenses

### 
# Main functions - sum_total, add_expenses, validate and gen_post_id
### 

def sum_total(exp):
    '''
    Function that calculates total value of items from passed expense list
    
    Args:
        exp(dict): Dictionary from JSON file, that contains keys and value elements

    Return:
        qtTotal(Decimal): Total amount of expenses, calculated by each row of expense
        items(int): List of items
    '''
    if not exp:
        return None
    total = Decimal("0.00")
    items = 0
    for sum in exp:
        try:
            total += Decimal(sum.get("amount", "0"))
            items += 1
        except (InvalidOperation, TypeError):
            raise ValueError("Nekorekta summa sarakstā")
    qtTotal = total.quantize(Decimal("0.01")) 
    return qtTotal, items



def gen_post_id():
    '''
    Function that checks and generates expense ID which is saved on data JSON
    
    Return:
        1(int): If there is no entries in expense list returns 1
        max(existing_ids) + 1: If there is an entries, gets latest ones id and adds 1 to that and returns the value
    '''
    expenses = load_expenses()
    if not expenses:
        return 1
    else: 
      existing_ids = [int(x.get("id", 0)) for x in expenses]
      return max(existing_ids) + 1

def add_expenses(expense):
    '''
    Function adds passed expense to an expense list, adding ID
    
    Args
        expense: Passed list of entries that is appended to existing list

    Return: 
        bool: True if data succesfully added, False otherwise
    '''
    expense["id"] = gen_post_id()
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    return True

def get_all_expenses():
    '''Display all expenses in a formatted table output'''
    expenses = load_expenses()
    total, count = sum_total(expenses)
    if not expenses:
        return ["Nav saglabātu izdevumu."]
    
    lines = []
    lines.append("\n" + "-" * 120)
    lines.append(f"{'#':<3} | {'Datums':<10} | {'Kategorija':<16} | {'Dok.nr.':<10} | {'Summa':<8} | {'Apraksts':<35} | {'Maksājuma veids':<10}")
    lines.append("-" * 120)

    for idx, item in enumerate(expenses, start=1):
        date = item.get("date", "N/A")
        category = item.get("category", "N/A")
        docID = item.get("docID", "N/A")
        amount = item.get("amount", 0)
        description = item.get("description", "N/A")
        paymentMeth = item.get("paymentMeth", "N/A")

        try: 
            lines.append(f"{idx}. | {date:<10} | {category:<16} | {docID:<10} | {amount:<8.2f} | {description:<35} | {paymentMeth:<10}")
        except (TypeError, ValueError) as e:
            lines.append(f"⚠ Kļūda rindā {idx}: {e}")
    
    lines.append("-" * 120 + "\n")
    lines.append(f"Kopā {total:<3.2f} EUR ({count} ieraksti)\n")
    return lines

def validate(field_type):
    '''
    Function that acts as helper function for adding data to database, currently JSON
    Main puprose is to handle passed field type and validate passed inputs, data to match set flags

    Args:
        field_type(str): Specify what kind of field type and validation flags needs to be used based on passed string, that also is validated

    Return:
        value(str/Decimal): Returns validated input to be passed for saving in database
    '''
    CATEGORIES = [
        "Ēdiens",
        "Transports",
        "Izklaide",
        "Komunālie maksājumi",
        "Veselība",
        "Iepirkšanās",
        "Cits",
    ]

    PAYMENT_METHODS = [
        "Skaidra nauda",
        "Bankas karte",
        "Pārskaitījums"
    ]

    field_fillers = {
        "date": "Datums (YYYY-MM-DD): ",
        "category": "Kategorija: ",
        "amount": "Summa (EUR): ",
        "docID": "Maksājuma apliecinājums",
        "description": "Apraksts: ",
        "paymentMeth": "Maksājuma veids: "
    }

    while True:
        value = input(field_fillers.get(field_type, "")).strip()

        if field_type == "date":
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return value
            except ValueError:
                raise ValueError("Nepareizs datuma formāts! Izmanto YYYY-MM-DD")  
        
        elif field_type == "category":
            if value in CATEGORIES:
                return value
            raise ValueError(f"Neatbilstoša kategorija! Izvēlies no: {', '.join(CATEGORIES)}")
        
        elif field_type == "amount":
            try:
                amount = Decimal(value)
                if amount <= 0:
                    raise ValueError("Summai jābūt pozitīvam skaitlim!")
                return Decimal(value)
            except ValueError:
                raise ValueError("Summai jābūt skaitlim!")
        
        elif field_type == "docID":
            if not value:
                raise ValueError("Maksājuma apliecinājums nedrīkst būt tukšs!")
            expenses = load_expenses()
            existing_ids = [e.get("docID") for e in expenses]
            
            if value in existing_ids:
                raise ValueError(f"Maksājuma apliecinājums '{value}' jau ir iekļauts sarakstā!")
            return value
        
        elif field_type == "description":
            if not value:
                raise ValueError("Apraksts nedrīkst būt tukšs!")
            return value
        
        elif field_type == "paymentMeth":
            if value in PAYMENT_METHODS:
                return value
            raise ValueError(f"Neatbilstošs maksājuma veids! Izvēlies no: {', '.join(PAYMENT_METHODS)}")
            
# Filtering

def filter_by_month(var):
    '''Return formatted expenses for a specific month'''
    expenses = load_expenses()

    if len(var) != 7 or var[4] != "-":
        raise ValueError("Formātam jābūt YYYY-MM")
    try: 
        year = int(var[:4])
        month = int(var[5:7])
        if not 1 <= month <= 12:
            raise ValueError("Menesim jābūt no 1 līdz 12")
    except ValueError:
        raise ValueError("Nepareizs datuma formāts! Izmanto YYYY-MM")
    
    filtered = [e for e in expenses if e.get("date", "").startswith(var)]

    if not filtered:
        return [f"Nav izdevumu mēnesim {var}"]

    total = sum(Decimal(str(e.get("amount", 0))) for e in filtered)

    rows = [
        f"{i}. | {e['date']:<10} | {e['category']:<16} | {e['docID']:<10} | {Decimal(str(e['amount'])):<8.2f} | {e['description']:<35} | {e['paymentMeth']:<10}"
        for i, e in enumerate(filtered, 1)
    ]

    return "\n".join([
        "\n" + "-"*120,
        f"{'#':<3} | {'Datums':<10} | {'Kategorija':<16} | {'Dok.nr.':<10} | {'Summa':<8} | {'Apraksts':<35} | {'Maksājuma veids':<10}",
        "-"*120,
        *rows,
        "-"*120,
        f"Kopā {total:.2f} EUR ({len(filtered)} ieraksti)\n"
    ])



def sum_by_categories():
    '''Calculates and returns a list of used categories that has expenses'''
    totals = {}

    for e in load_expenses():
        cat= e.get("category", "N/A")
        amount = Decimal(str(e.get("amount", 0)))
        totals[cat] = totals.get(cat, Decimal("0")) + amount
    
    lines = []
    lines.append("\nKategoriju kopsavilkums")
    lines.append("-" * 40)
    catTotals = 0

    for cat, total in totals.items():
        lines.append(f"{cat:<20} {total:>8.2f} EUR")
        catTotals += total

    lines.append("-" * 40)
    lines.append("Kopā:" + " " * 18 + f"{catTotals:.2f} EUR")
    lines.append("-" * 40)

    return "\n".join(lines)
    

# Function for returning months with expenses
def get_available_months():
    '''Return a list of available months from expenses'''
    expenses = load_expenses()
    if not expenses:
        return []
    
    months = {}
    for expense in expenses:
        date = expense.get("date", "")
        if date:
            month = date[:7] # YYYY-MM
            months[month] = months.get(month, 0) + 1
    
    return sorted(months.items())


# Delete an expense from list

def display_all_with_ids():
    '''Display all expenses with their IDs.'''
    expenses = load_expenses()
    if not expenses:
        return "Nav izdevumu."
    
    lines = []
    lines.append("\n" + "-"*120)
    lines.append(f"{'ID':<5} | {'Datums':<10} | {'Kategorija':<16} | {'Dok.nr.':<10} | {'Summa':<8} | {'Apraksts':<35} | {'Maksājuma veids':<10}")
    lines.append("-"*120)
    
    for e in expenses:
        line = f"{e.get('id'):<5} | {e['date']:<10} | {e['category']:<16} | {e['docID']:<10} | {Decimal(str(e['amount'])):<8.2f} | {e['description']:<35} | {e['paymentMeth']:<10}"
        lines.append(line)
    
    lines.append("-"*120 + "\n")
    return "\n".join(lines)

def delete_expense(expID):
    '''Deletes expense that matches passed id'''
    expenses = load_expenses()
    new_expenses = [e for e in expenses if e.get("id") != expID]
    
    if len(new_expenses) == len(expenses):
        return False
    
    save_expenses(new_expenses)
    return True
