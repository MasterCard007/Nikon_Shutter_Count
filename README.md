# Nikon NEF Shutter Count Reader
This Python script is designed to read the shutter count from Nikon NEF (RAW) files. It's particularly useful for photographers who wish to check the number of actuations (shutter releases) of their Nikon cameras.

Features
Automatically finds NEF files in the current directory.
If multiple NEF files are present, it selects the most recently modified file.
Retrieves the shutter count from the file's EXIF data.
Requirements
Python 3
exifread library
Installation
Ensure Python 3 is installed on your system. You can download it from python.org.

Install the exifread library. This can be done via pip:

bash
Copy code
pip install exifread
Usage
Place the script in the directory containing your NEF file(s).

Run the script using Python:

bash
Copy code
python shutter_count.py
The script will automatically find the latest NEF file in the directory and display its shutter count.

Note
The script assumes that the EXIF tag for the shutter count is MakerNote TotalShutterReleases. This might vary based on the camera model and firmware.

The script works best with files directly from the camera. Transferred or modified files might not contain all the necessary EXIF data.
