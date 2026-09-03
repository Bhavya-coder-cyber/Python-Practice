import os
import json

INPUT_FILE = "data.json"
OUTPUT_FILE = "flattened_data.json"

def flatten_json(data, parent=""):
    items = {}

    if isinstance(data, dict):
        for k,v in data.items():
            flatten_value = f"{parent}.{k}" if parent else k
            items.update(flatten_json(v, flatten_value))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            flatten_value = f"{parent}.{idx}" if parent else str(idx)
            items.update(flatten_json(item, flatten_value))
    else:
        items[parent] = data
        
    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"JSON file not found")
        return

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        flattened_data = flatten_json(data)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(flattened_data, f, indent=2)
        print(f"Successfully converted to {OUTPUT_FILE}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()