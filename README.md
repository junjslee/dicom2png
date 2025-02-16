# DICOM to PNG

A simple Python tool to convert DICOM files to PNG images. Saves the dicom files into designated output directory and prints the total number of files converted.

## Usage
```bash
python dicom_to_png.py --input_dir dicom_files --output_dir png_output
```
If the directories are not specified, the script uses the defaults:
- Input directory: dicom_files
- Output directory: png_output
After running, the script will output the number of DICOM files converted.