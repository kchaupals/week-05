Latviski
======
# 🤑 Izdevumu izsekotājs komandrindas saskarne

Vienkārša komandrindas Python saskarnes aplikācija, lai sekotu personigajiem izdevumiem ar JSON krātuvi, CSV/TXT eksporta opcijam un precīzu decimalo formatējumu naudai.

## 📦 Iespējas
- Pievienot, apskatīt un dzēst izdevumus
- Izdevumi tiek glabāti JSON failā (expenses.json)
- Iespējams eksportēt sarakstu kā CSV (Excel) vai TXT(vienkārša teksta failā)
- Eksporta faili ir ar laika zīmogu un atrodas direktorijā - exports/
- Komandrindas izvēlnes opcija vieglai navigācijai

## 🏗 Projekta struktūra
```
expense-tracker/
│
├─ app.py          # Komandrindas izvēlne un lietotāja mijiedarbība
├─ export.py       # Eksporta loģika (CSV/TXT)
├─ storage.py      # JSON ielasišanas un rakstīšanas funkcijas
├─ logic.py        # Biznesa loģikas funkcijas
├─ expenses.json   # Lokāls datu uzglabāšanas fails (Izveidojas automātiski)
├─ exports/        # Eksportētie CSV/TXT faili saglabājas šeit
└─ README.md
```

## 🚀 Kā uzsākt lietot
1. Noklonē šo repozitoriju
```bash
git clone https://github.com/kchaupals/week-05.git expense-tracker
cd expense-tracker
```
2. Palaid aplikācijas failu:
```bash
python app.py
```

## 📖 Komandas 
```
| Izvēle | Funkcija                      |
| ------ | ----------------------------- |
| 1      | Pievienot izdevumu            |
| 2      | Apskatīt izdevumus            |
| 3      | Filtrēt pēc mēneša            |
| 4      | Kopsavilkums pa kategorijām   |
| 5      | Dzēst izdevumu                |
| 6      | Eksportēt izdevumus (CSV/TXT) |
| 7      | Iziet                         |
```

## ➕ Izdevuma pievienošana
Tiek prasīts:
- Datums (YYYY-MM-DD)
- Kategorija (Definēti robežgadījumi logic.py)
- Summa (Decimals skaitlis)
- Maksājuma apliecinājuma dokumenta nr.
- Apraksts
- Maksājuma veids (Skaidra nauda, Bankas karte, Pārskaitījums)

Piemērs:
```
Datums: 2026-03-03
Kategorija: Ēdiens
Summa: 19.99
Maksājuma apliecinājums: DOC123
Apraksts: Pusdienas
Maksājuma veids: Bankas karte
```

## Autors

> Kārlis Čaupals -- Programmēšanas pamati, 2026


ENGLISH 
======

# 🤑 Expense Tracker CLI

A **simple command-line Python app** to track personal expenses with JSON storage, CSV/TXT export and precise decimal handling for money

## 📦 Features
- Add, view and delete expenses
- Expenses stored in JSON (expenses.json)
- Export expenses to CSV (Excel-compatible) or TXT (human-readable)
- Timestamped export files stored in exports/
- CLI menu-driven interface for easy navigation

## 🏗 Project Structure
```
expense-tracker/
│
├─ app.py          # CLI menu and user interaction
├─ export.py       # Export logic (CSV/TXT)
├─ storage.py      # JSON load/save functions
├─ logic.py        # Bussiness logic functions
├─ expenses.json   # Local storage file (auto-created)
├─ exports/        # Exported CSV/TXT files saved here
└─ README.md
```

## 📖 Commands 
```
| Option | Action                    |
| ------ | ------------------------- |
| 1      | Add expense               |
| 2      | View expenses             |
| 3      | Filter by month           |
| 4      | Categories summary        |
| 5      | Delete expense            |
| 6      | Export expenses (CSV/TXT) |
| 7      | Exit                      |
```

## ➕ Adding an Expense
Prompted for:
- Date (YYYY-MM-DD)
- Category(There pre-defined list in logic.py)
- Amount (Decimal)
- Payment Document ID
- Description
- Payment Method (Cash, Card, Bank Transfer)

Example:
```
Date: 2026-03-03
Category: Food
Amount: 19.99
DocID: DOC123
Description: Lunch
Paymenth Method: Card
```

## Author

> Kārlis Čaupals - Programming basics, 2026