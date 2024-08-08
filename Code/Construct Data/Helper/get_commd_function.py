import json 
import subprocess
import csv
from os.path import isfile

import os

IDA_PATH32 = "D:\\IDA\\IDAPro6.6\\idaq.exe"
IDA_PATH64 = "D:\\IDA\\IDAPro6.6\\idaq64.exe"
IDA_PLUGIN = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\IDA_scrips_disassmbly.py"


list_folders=["clamav", "curl", "nmap", "openssl", "unrar", "zlib"]

save_directory = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\functions"
csv_folder_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\CSV"
idbs_folder = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs"


with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\vocab_function.json") as josn_file:

    data = json.load(josn_file)



def explort_json_32(idb_path,  file_name, file_path):  
    if  isfile(idb_path):       
        cmd = [IDA_PATH32,
                '-A',
                # '-L{}'.format(LOG_PATH),
                '-S{}'.format(IDA_PLUGIN),
                '-Ofile_name:{}@{}'.format(file_name, file_path),
                idb_path]

        print("[D] cmd: {}".format(cmd))

        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        if proc.returncode == 0:
            print("[D] {}: success".format(idb_path))
        else:
            print("[!] Error in {} (returncode={})".format(
                idb_path, proc.returncode))
    else:
        print("[!] Error: {} does not exist".format(idb_path))

def explort_json_64(idb_path,  file_name, file_path):  
    if  isfile(idb_path):       
        cmd = [IDA_PATH64,
                '-A',
                # '-L{}'.format(LOG_PATH),
                '-S{}'.format(IDA_PLUGIN),
                '-Ofile_name:{}@{}'.format(file_name, file_path),
                idb_path]

        print("[D] cmd: {}".format(cmd))

        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        if proc.returncode == 0:
            print("[D] {}: success".format(idb_path))
        else:
            print("[!] Error in {} (returncode={})".format(
                idb_path, proc.returncode))
    else:
        print("[!] Error: {} does not exist".format(idb_path))

#64 

# file_64 = []
# file_32 = []
# folder = 'nmap'
# with open(csv_folder_path +"//64//"+ folder + ".csv") as csv_file64:
#     reader = csv.reader(csv_file64)

#     file_64 = [row[0] for row in reader]

# with open(csv_folder_path +"//32//"+ folder + ".csv") as csv_file32:
#     reader = csv.reader(csv_file32)

#     file_32 = [row[0] for row in reader]

# print(file_32[:5])
# print(file_64[:5])


                




for folder  in list_folders[1:]:
    path_save_work_dir = os.path.join(save_directory, folder)
    if not os.path.exists(path_save_work_dir):
        os.makedirs(path_save_work_dir)
    
    file_64 = []
    file_32 = []
    with open(csv_folder_path +"//64//"+ folder + ".csv") as csv_file64:
        reader = csv.reader(csv_file64)

        file_64 = [row[0] for row in reader]

    with open(csv_folder_path +"//32//"+ folder + ".csv") as csv_file32:
        reader = csv.reader(csv_file32)

        file_32 = [row[0] for row in reader]
    
    functions = data[folder]
    for funct in functions:
        temp_save_dir = os.path.join(path_save_work_dir, funct)
        if not os.path.exists(temp_save_dir):
            os.makedirs(temp_save_dir)

        for file_name in file_64:
            if funct in file_name:
                idb_path = os.path.join(idbs_folder, folder, "64", file_name + ".i64")
                explort_json_64(idb_path, file_name, temp_save_dir)

        for file_name in file_32:
            if funct in file_name:
                idb_path = os.path.join(idbs_folder, folder, "32", file_name + ".idb")
                explort_json_32(idb_path, file_name, temp_save_dir)

        
        
        
        

        


    


#get common function 32 bits

#get common function 64 bits



