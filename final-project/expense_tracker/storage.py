# Utility to work with saving and loading data

# Standart libs
import os
import json
import platform
import csv
import subprocess
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

# Local modules
import logic

# Setting up ENV

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# External lists 
EXPORT_DIR = BASE_DIR / "exports"
LISTS_DIR = BASE_DIR / "lists"

# Ensures directories mentioned above exists
for directory in (EXPORT_DIR, LISTS_DIR):
    directory.mkdir(parents=True, exist_ok=True)

# Main data storage between sessions
DEFAULT_STORAGE = BASE_DIR / "expenses.json"

# Loading files from which lists are retrived

def load_expenses():
    '''Function to load expense list from JSON'''
    if not DEFAULT_STORAGE.exists():
       return []
    
    try:
        with DEFAULT_STORAGE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decode error in {DEFAULT_STORAGE}: {e}")
    
    except OSError as e:
        raise OSError(f"File error with {DEFAULT_STORAGE}: {e}")



def save_expenses(expenses):
    '''Save the given expenses list to JSON'''
    DEFAULT_STORAGE.parent.mkdir(parents=True, exist_ok=True)

    with DEFAULT_STORAGE.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)




