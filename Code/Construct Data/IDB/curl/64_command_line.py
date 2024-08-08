import csv 
import subprocess
from os.path import isfile



files = []
with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\curl_csv_file_64bits.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        files.append(row[0].strip())
'''
D:\IDA\IDAPro6.6>idaq64.exe -a- -B 
-o"D:\HocTap\HK2_2023_2024\ML\Project\Dataset\test\arm64-clang-9-Os_curl.i64" D:\HocTap\HK2_2023_2024\ML\Project\Dataset\Dataset-1\Dataset-1\curl\arm64-clang-9-Os_curl
'''
# with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\IDB\\curl\\idb_command_64.csv", "w", newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     for f in files:
#         command_line=""
#         command_line = "D:\\IDA\\IDAPro6.6\\idaq64.exe -a- -B"
#         command_line += f' -o"D:\HocTap\HK2_2023_2024\ML\Project\Dataset\IDBs\curl{f}.i64"'
#         command_line += ' D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\Dataset-1\\Dataset-1\\curl\\'
#         command_line += str(f)
#         writer.writerow([command_line], )

IDA_PATH = "D:\\IDA\\IDAPro6.6\\idaq64.exe"

def export_idb(input_path, output_path):
    """Launch IDA Pro and export the IDB. Inner function."""
    try:
        print("Export IDB for {}".format(input_path))
        ida_output = str(subprocess.check_output([
            IDA_PATH,
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

for f in files:
    input_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\Dataset-1\\Dataset-1\\curl\\" + f
    output_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs\\curl\\" + str(f) + ".i64"
    export_idb(input_path, output_path)



        