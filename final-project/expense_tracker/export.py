# Includes default libraries
from datetime import datetime
from decimal import Decimal, InvalidOperation
import os
import csv
import platform
import subprocess

# Includes local module
import storage
from logic import sum_total

def export_list(file_type="csv", filename=None):
    '''Export the current shopping list to CSV or text'''
    expenses = storage.load_expenses()
    total, count = sum_total(expenses)

    if not expenses:
        return False
    
    # Creating timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if filename:
        base_name = filename
    else:
        base_name = "izdevumi"
    
    full_filename = f"{base_name}_{timestamp}.{file_type}"
    full_path = os.path.join(storage.EXPORT_DIR, full_filename)

    # ------------ CSV ------------
    if file_type == "csv":
        with open(full_path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["","ID","Datums", "Kategorija", "Maksājuma apliecinājums", "Summa", "Apraksts", "Maksājuma veids"])
            for idx, item in enumerate(expenses, 1):
                id = item["id"]
                date = item["date"]
                category = item["category"]
                docID = item["docID"]
                description = item["description"]
                amount = Decimal(item["amount"])
                paymentMeth = item["paymentMeth"]
                writer.writerow([idx, id, date, category, docID,f"{amount:.2f}", description, paymentMeth])
            writer.writerow([f"Kopēja summa:",f"{total:.2f} EUR",f"({count} izdevumi)"])
        auto_open(full_path)
        return True
    # ------------ TXT ------------
    elif file_type == "txt":
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(f"Izdevumu saraksts: {base_name}\n")
            f.write(f"Eksportēts: {timestamp}\n")
            f.write("-"* 50 + "\n")
            for idx, item in enumerate(expenses,1):
                id = item["id"]
                date = item["date"]
                category = item["category"]
                docID = item["docID"]
                description = item["description"]
                amount = Decimal(item["amount"])
                paymentMeth = item["paymentMeth"]
                f.write(f"{idx}. ID:{id}| Datums: {date:<7} | Kategorija: {category:>3} | Maksājuma apliecinājums: {docID:>4} | Apraksts: {description:>3} | Summa: {amount:.2f} | Maksājuma veids {paymentMeth} \n")
            f.write("-"* 50 + "\n")
            f.write(f"Kopēja summa {total:.2f} EUR ({count} izdevumi)")
        auto_open(full_path)
        return True
    else:
        return False
    
def auto_open(file_path):
    try:
        system = platform.system()
        if system == "Windows":
            os.startfile(file_path)
        elif system == "Darwin": # macOS
            subprocess.run(["open", file_path])
        else: # Linux
            subprocess.run(["xdg-open", file_path])
    except Exception:
        raise Exception("⚠ Nevar automātiski atvērt failu")