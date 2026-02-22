#!/usr/bin/env python3
"""Converting CSV to JSON"""

import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path):
    """Convert a CSV file to a JSON file."""
    try:
        data = []

        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file)
        
        return True
    
    except Exception:
        return False