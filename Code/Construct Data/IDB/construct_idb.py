
import os
import subprocess
from os.path import isfile
import csv

list_folders=["clamav", "curl", "nmap", "openssl", "unrar", "z3", "zlib"]

IDA_PATH32 = "D:\\IDA\\IDAPro6.6\\idaq.exe"
IDA_PATH64 = "D:\\IDA\\IDAPro6.6\\idaq64.exe"

def export_idb_32(input_path, output_path):
    """Launch IDA Pro and export the IDB. Inner function."""
    try:
        print("Export IDB for {}".format(input_path))
        ida_output = str(subprocess.check_output([
            IDA_PATH32,
            # "-L{}".format(LOG_PATH),  # name of the log file. "Append mode"
            "-a-",  # enables auto analysis
            "-B",  # batch mode. IDA will generate .IDB and .ASM files
            "-o{}".format(output_path),
            input_path
        ]))

        if not isfile(output_path):
            print("[!] Error: file {} not found".format(output_path))
            print(ida_output)
            return False

        return True

    except Exception as e:
        print("[!] Exception in export_idb\n{}".format(e))

def export_idb_64(input_path, output_path):
    """Launch IDA Pro and export the IDB. Inner function."""
    try:
        print("Export IDB for {}".format(input_path))
        ida_output = str(subprocess.check_output([
            IDA_PATH64,
            # "-L{}".format(LOG_PATH),  # name of the log file. "Append mode"
            "-a-",  # enables auto analysis
            "-B",  # batch mode. IDA will generate .IDB and .ASM files
            "-o{}".format(output_path),
            input_path
        ]))

        if not isfile(output_path):
            print("[!] Error: file {} not found".format(output_path))
            print(ida_output)
            return False

        return True

    except Exception as e:
        print("[!] Exception in export_idb\n{}".format(e))


# for file in file_name:
#     if not os.path.exists("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs\\" + file):
#         os.makedirs("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs\\" + file)
#     if not os.path.exists("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs\\" + file +"\\64"):
#         os.makedirs("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs\\" + file + "\\64")
#     if not os.path.exists("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs\\" + file +"\\32"):
#         os.makedirs("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs\\" + file + "\\32")

#clamav

file_names = []
with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\CSV\\32\\openssl.csv", "r") as clamav_csv:
    reader = csv.reader(clamav_csv)
    for row in reader:
        file_names.append(row[0])

#x64
for f in file_names:
    input_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\Dataset-1\\Dataset-1\\openssl\\" + f
    output_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs\\openssl\\32\\" + f + ".idb"

    export_idb_32(input_path, output_path)
