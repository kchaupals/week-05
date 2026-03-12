# Utility to work with saving and loading data from database - JSON
# Standart libs
import json
from decimal import Decimal
from pathlib import Path

# Setting up ENV
# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# External directories
EXPORT_DIR = BASE_DIR / "exports"
LISTS_DIR = BASE_DIR / "lists"

# Ensures directories mentioned above exists, if no - creates them automatically
for directory in (EXPORT_DIR, LISTS_DIR):
    directory.mkdir(parents=True, exist_ok=True)

# Main data storage file between sessions
DEFAULT_STORAGE = BASE_DIR / "expenses.json"

# Loading data from an JSON file or automatically creating empty one if not found

def load_expenses():
    '''Function to load expense list from JSON'''
    if not DEFAULT_STORAGE.exists():
       return []
    
    try:
        with DEFAULT_STORAGE.open("r", encoding="utf-8") as f:
            expenses = json.load(f)
        
        for item in expenses:
            if "amount" in item:
                item["amount"] = Decimal(item["amount"])
                
        return expenses
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decode error in {DEFAULT_STORAGE}: {e}")
    
    except OSError as e:
        raise OSError(f"File error with {DEFAULT_STORAGE}: {e}")

# Saving data to an JSON file, also creating file if there is none
def save_expenses(expenses):
    '''Save the given expenses list to JSON'''
    DEFAULT_STORAGE.parent.mkdir(parents=True, exist_ok=True)

    with DEFAULT_STORAGE.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False, default=str)



if __name__ == "__main__":
    print("Utility to work with saving and loading data from database - JSON")
    print("\nFunctions:")
    print('''
    # load_expenses() - Loading data from an JSON file or automatically creating empty one if not found
    # save_expenses() - Saving data to an JSON file, also creating file if there is none
    ''')
