import os
from exifread import process_file

def find_latest_nef_file():
    nef_files = [file for file in os.listdir('.') if file.lower().endswith('.nef')]
    if not nef_files:
        return None

    latest_nef_file = max(nef_files, key=os.path.getmtime)
    return latest_nef_file

def get_camera_info(nef_file):
    with open(nef_file, 'rb') as f:
        data = process_file(f)

        # Get the shutter count
        shutter_count = data.get("MakerNote TotalShutterReleases", "not found--make sure to use file straight from camera")

        # Get the camera name
        make = data.get("Image Make", "Unknown Make")
        model = data.get("Image Model", "Unknown Model")
        camera_name = f"{make} {model}".strip()

        # Get the timestamp
        timestamp = data.get("EXIF DateTimeOriginal", "Unknown Timestamp")

        return shutter_count, camera_name, timestamp

def main():
    nef_file = find_latest_nef_file()

    if nef_file:
        print(f"Using NEF file: {nef_file}")
        shutter_count, camera_name, timestamp = get_camera_info(nef_file)
        print(f"Camera Name: {camera_name}")
        print(f"Timestamp: {timestamp}")
        print(f"Shutter Count: {shutter_count}")
    else:
        print("No NEF file found in the current directory.")

if __name__ == "__main__":
    main()
