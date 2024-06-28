# This function helps to test individual functionalities
import zlib
import zipfile
import os

def compress(file_names):
    print("File Paths:")
    print(file_names)

    # Select the compression mode ZIP_DEFLATED for compression
    # or zipfile.ZIP_STORED to just store the file
    compression = zipfile.ZIP_DEFLATED

    # create the zip file first parameter path/name, second mode
    zf = zipfile.ZipFile(os.getcwd() + "\\RAWs.zip", mode="w")
    try:
        for file_name in file_names:
            # Add file to the zip file
            # first parameter file to zip, second filename in zip
            file_name1 = file_name.split('\\')[-1]

            zf.write(file_name, file_name1, compress_type=compression)

    except FileNotFoundError:
        print("An error occurred")
    finally:
        # Don't forget to close the file!
        zf.close()


file_names= [os.getcwd() + "\\text_file.txt", os.getcwd() + "\\text_file2.txt"]
compress(file_names)