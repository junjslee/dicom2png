import os
import argparse
import pydicom
import numpy as np
import matplotlib.pyplot as plt

def convert_dicom_to_png(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    converted_count = 0

    # Loop over each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".dcm"):
            dicom_path = os.path.join(input_dir, filename)
            try:
                # Read the DICOM file
                ds = pydicom.dcmread(dicom_path)
                # Get the image pixel array
                image = ds.pixel_array.astype(float)
                # Normalize the pixel values to the range 0-255
                image = (np.maximum(image, 0) / image.max()) * 255.0
                image = np.uint8(image)
                
                # Create the PNG file name and path
                png_filename = os.path.splitext(filename)[0] + ".png"
                png_path = os.path.join(output_dir, png_filename)
                
                # Save the image as PNG using a grayscale colormap
                plt.imsave(png_path, image, cmap="gray")
                converted_count += 1
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

    print(f"Converted {converted_count} DICOM files to PNG.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert DICOM files to PNG images.")
    parser.add_argument("--input_dir", type=str, default="dicom_files",
                        help="Directory containing DICOM files (default: dicom_files)")
    parser.add_argument("--output_dir", type=str, default="png_output",
                        help="Directory to save PNG files (default: png_output)")
    args = parser.parse_args()

    convert_dicom_to_png(args.input_dir, args.output_dir)