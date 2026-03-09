# Utility to handle bussiness logic and calculations

# Import standart libs
from decimal import Decimal, InvalidOperation
from datetime import datetime

# Import local modules
from storage import load_expenses, save_expenses



def sum_total():
    expenses = load_expenses()
    if not expenses:
        return None
    total = Decimal("0.00")
    for sum in expenses:
        try:
            total += Decimal(sum.get("amount", "0"))
        except (InvalidOperation, TypeError):
            raise ValueError("Nekorekta summa sarakstā")
    qtTotal = total.quantize(Decimal("0.01")) 
    return qtTotal



def gen_post_id():
    expenses = load_expenses()
    if not expenses:
        return 1
    else: 
      existing_ids = [int(x.get("id", 0)) for x in expenses]
      return max(existing_ids) + 1

def add_expenses(expense):
    expense["id"] = gen_post_id()
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    return True

def get_all_expenses():
    '''Display all expenses in a table'''
    expenses = load_expenses()
    if not expenses:
        return ["Nav saglabātu izdevumu."]
    
    lines = []
    lines.append("\n" + "-" * 120)
    lines.append(f"{'#':<3} | {'Datums':<10} | {'Kategorija':<8} | {'Dok.nr.':<10} | {'Summa':<8} | {'Apraksts':<35} | {'Maksājuma veids':<10}")
    lines.append("-" * 120)

    for idx, item in enumerate(expenses, start=1):
        date = item.get("date", "N/A")
        category = item.get("category", "N/A")
        docID = item.get("docID", "N/A")
        amount = item.get("amount", 0)
        description = item.get("description", "N/A")
        paymentMeth = item.get("paymentMeth", "N/A")

        try: 
            lines.append(f"{idx}. | {date:<10} | {category:<8} | {docID:<10} | {amount:<8.2f} | {description:<35} | {paymentMeth:<10}")
        except (TypeError, ValueError) as e:
            lines.append(f"⚠ Kļūda rindā {idx}: {e}")
    
    lines.append("-" * 120 + "\n")
    return lines

# Validation 

def validate(field_type):
    '''Validate input that is specified'''
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
