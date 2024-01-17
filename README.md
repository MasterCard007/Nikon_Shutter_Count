
# NEF File Shutter Count Reader

This Python script provides a simple way to read the shutter count from Nikon Electronic Format (NEF) files, typically used in Nikon cameras. The script searches for the latest NEF file in the current directory and extracts the shutter count from it.

## Features

- **Find Latest NEF File:** Locates the latest NEF file in the current directory.
- **Read Shutter Count:** Extracts the shutter count information from the NEF file.

## Prerequisites

Before running the script, ensure that you have the `exifread` package installed. If not, you can install it using pip:

```bash
pip install exifread
```

## Usage

To use the script, simply run it in a directory containing NEF files. The script will automatically find the latest NEF file and display its shutter count:

```bash
python shutter_count_reader.py
```

## How It Works

1. **Find the Latest NEF File:** The script searches the current directory for files with a `.nef` extension and selects the one with the latest modification time.
2. **Extract Shutter Count:** Opens the selected NEF file and reads the shutter count using the `exifread` package.

## Important Notes

- The script is designed to work with files directly from the camera. If the file has been modified or processed, the shutter count may not be accurately retrieved.
- The script currently only supports NEF files.

## Contributing

Feel free to fork this project and contribute. Your contributions for supporting more file formats or enhancing functionality are welcome!

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
