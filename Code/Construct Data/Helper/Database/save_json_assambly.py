
import json
import os
from os.path import isfile
import subprocess
import csv
import pickle



common_function_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\results\\all_commom_funct.json"
folder_path_save = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\Database\\assambly_result"
idbs_folder = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\IDBs"
csv_folder_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\CSV"

with open(common_function_path, "r") as json_file:
    data = json.load(json_file)

with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\vocab_function.json") as josn_file:

    data_file_names = json.load(josn_file)


IDA_PATH32 = "D:\\IDA\\IDAPro6.6\\idaq.exe"
IDA_PATH64 = "D:\\IDA\\IDAPro6.6\\idaq64.exe"
IDA_PLUGIN = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\Database\\IDA_disass_functions.py"


list_softwares=["clamav", "curl", "nmap", "openssl", "unrar", "zlib"]

def explort_json_32(idb_path,  file_name, software_list):  
    if  isfile(idb_path):       
        cmd = [IDA_PATH32,
                '-A',
                # '-L{}'.format(LOG_PATH),
                '-S{}'.format(IDA_PLUGIN),
                '-Ofile_name:{}@{}'.format(file_name, software_list),
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

def explort_json_64(idb_path,  file_name, software_list):  
    if  isfile(idb_path):       
        cmd = [IDA_PATH64,
                '-A',
                # '-L{}'.format(LOG_PATH),
                '-S{}'.format(IDA_PLUGIN),
                '-Ofile_name:{}@{}'.format(file_name, software_list),
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


# for folder in list_folders:
#     function_lists = list(key for key in data[folder].keys())
#     for fucnt in function_lists:
#         print(folder, ": ", fucnt,": ",len(data[folder][fucnt]))

for software_name in list_softwares[1:]:
    path_save_work_dir = os.path.join(folder_path_save, software_name)
    if not os.path.exists(path_save_work_dir):
        os.makedirs(path_save_work_dir)

    sub_component_software_list = data_file_names[software_name]

    file_64 = []
    file_32 = []
    with open(csv_folder_path +"//64//"+ software_name + ".csv") as csv_file64:
        reader = csv.reader(csv_file64)

        file_64 = [row[0] for row in reader]

    with open(csv_folder_path +"//32//"+ software_name + ".csv") as csv_file32:
        reader = csv.reader(csv_file32)

        file_32 = [row[0] for row in reader]

    #64 bits
    for sub_component_software_name in sub_component_software_list:
        for file in file_64:
            if sub_component_software_name in file:

                file_name = file
                idb_file_path = os.path.join(idbs_folder, software_name, "64", file_name + ".i64")
                software_list = '&'.join([software_name, sub_component_software_name])
                explort_json_64(idb_path=idb_file_path, file_name=file_name, software_list=software_list)

        for file in file_32:
            if sub_component_software_name in file:

                file_name = file
                idb_file_path = os.path.join(idbs_folder, software_name, "32", file_name + ".idb")
                software_list = '&'.join([software_name, sub_component_software_name])
                explort_json_32(idb_path=idb_file_path, file_name=file_name, software_list=software_list)

    #32 bits

    


# with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\results\\all_commom_funct.json", "r") as file_funct:
#     data = json.load(file_funct)
# with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\results\\functions_list.pickle", "wb") as file:
#     pickle.dump(data, file)













