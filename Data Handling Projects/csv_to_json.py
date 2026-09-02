import os
import csv
import json

INPUT_FILE = 'data.csv'
OUTPUT_FILE = 'data.json'

def load_csv(filename):
    if not os.path.exists(filename):
        print(f"CSV file not found")
        return []

    with open(filename, 'r', encoding='utf-8') as f:
        try:
            reader = csv.DictReader(f)
            data = list(reader)
            return data
        except:
            pass

def convert_to_json(data, outputfile):
    if not data:
        print("No data found")
        return

    with open(outputfile, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"Successfully converted to {outputfile}")

def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2))
    print("*********")

def main():
    print("CSV to JSON Converter")
    data = load_csv(INPUT_FILE)
    convert_to_json(data, OUTPUT_FILE)
    preview_data(data)

if __name__ == "__main__":
    main()