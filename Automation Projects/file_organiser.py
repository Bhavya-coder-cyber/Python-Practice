import os
import shutil

EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".doc", ".docx", ".txt"],
    "Music": [".mp3", ".wav", ".flac"]
}

def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "Others"

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        if os.path.splitext(file)[1].lower() == ".py":
            continue
        
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            folder = get_destination_folder(file)
            dest_folder_path = os.path.join(folder_path, folder)

            os.makedirs(dest_folder_path, exist_ok=True)

            shutil.move(full_path, os.path.join(dest_folder_path, file))
            print(f"Moved {file} to {folder}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path or leave blank: ").strip()
    folder = folder_path or os.getcwd()

    if not os.path.isdir(folder):
        print(f"Invalid folder path: {folder}")
    else:
        sort_files(folder)
        print("File sorting completed.")
    