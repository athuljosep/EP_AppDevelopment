# This function helps to test individual functionalities
import shutil


file1_path = 'ASHRAE901_OfficeSmall_STD2013_Seattle.idf'
file2_path = 'Special.idf'

with open(file2_path, 'r') as file2:
    with open(file1_path, 'a') as file1:
        shutil.copyfileobj(file2, file1)
