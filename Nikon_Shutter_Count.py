import os
from exifread import process_file

def find_latest_nef_file():
    nef_files = [file for file in os.listdir('.') if file.lower().endswith('.nef')]
    
    if not nef_files:
        return None

    # Sort files by last modified time and return the latest
    latest_nef_file = max(nef_files, key=os.path.getmtime)
    return latest_nef_file

def get_shutter_count(nef_file):
    with open(nef_file, 'rb') as f:
        data = process_file(f)
        shutter_count = data.get("MakerNote TotalShutterReleases", "not found--make sure to use file straight from camera")
        return shutter_count

def main():
    nef_file = find_latest_nef_file()

    if nef_file:
        print(f"Using NEF file: {nef_file}")
        shutter_count = get_shutter_count(nef_file)
        print(f"Shutter Count: {shutter_count}")
    else:
        print("No NEF file found in the current directory.")

if __name__ == "__main__":
    main()
