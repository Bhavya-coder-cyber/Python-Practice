import os 

def batch_name(folder, base_name, extension):
    files = [f for f in os.listdir(folder) if f.lower().endswith(extension.lower())]
    files.sort()

    if not files:
        print("No files found")
        return

    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"{file} => {new_name}")
    choice = input("Press (y) to confirm or (n) to reject: ").strip().lower()
    if choice != "y":
        return

    for i, file in enumerate(files, start=1):
        old_path = os.path.join(folder, file)
        new_name = f"{base_name}_{i}{extension}"
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
    print(f"Renamed {len(files)} successfully")

if __name__ == "__main__":
    folder = input("Enter the folder path or leave blank: ").strip() or os.getcwd()

    if not os.path.isdir(folder):
        print(f"Invalid folder path: {folder}")
    else:
        base_name = input("Enter the base name: ").strip()
        extension = input("Enter the extension: ").strip()

        batch_name(folder, base_name, extension)
    