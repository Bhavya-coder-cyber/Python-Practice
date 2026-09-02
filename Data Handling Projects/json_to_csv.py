import os
import json
import csv

INPUT_FILE = 'data.json'
OUTPUT_FILE = 'data.csv'

def load_json_file(filename):
    if not os.path.exists(filename):
        print(f"JSON file not found")
        return []

    with open(filename, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            pass

def convert_to_csv(data, outputfile):
    if not data:
        print("No data found")
        return

    fieldname = list(data[0].keys())
    with open(outputfile, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

    print(f"Successfully converted to {outputfile}")

def main():
    print("JSON to CSV Converter")
    data = load_json_file(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if "__name__" == "__main__":
    main()