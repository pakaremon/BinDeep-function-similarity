import pickle
import idaapi

import idautils
import idc

import pickle
import os
import json
import re
import sqlite3

from os.path import isfile


database_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\Database\\bin_similar.db"

with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\results\\functions_list_IDA.pkl", "rb") as file:
    data = pickle.load(file)

list_of_function=[]

print("===start program====")

FUNNCTION_NAME=""
cursor = 0
real_names = []
addresses = []
names = idautils.Functions()


for n in names:
    funcName = idc.GetFunctionName(n)
    real_names.append(funcName )
    addresses.append(n)



def get_dis_asm_by_function(fuction_name):
    list_of_instructions = []
    cursor = None
    for rn in real_names:
        if rn == fuction_name:
            print(real_names.index(fuction_name))

            cursor = addresses[int(real_names.index(fuction_name))]
            break

    if cursor:
        myFunc = idaapi.get_func(cursor)
        while cursor < myFunc.endEA:
            list_of_instructions.append(idc.GetDisasm(cursor))
            cursor = idc.NextHead(cursor, myFunc.endEA)

    return list_of_instructions


def main(file_name, software_list):

    matches = re.search(r'^(x86|x64|arm32|arm64).+$', file_name,re.IGNORECASE)
    if matches:
        architecture = matches.group(1)
    

    

    software_list = software_list.split('&')
    software_name = software_list[0]
    sub_software_name = software_list[1]

    list_of_function =   data[software_name][sub_software_name]

    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    list_item_binary = file_name.split('-')

    binary_name = list_item_binary[-1]
    architecture = list_item_binary[0]
    compiler = list_item_binary[1]
    compiler_version = list_item_binary[2]

    cur.execute("INSERT INTO binary_name (binary_name, architecture, compiler, compiler_version) VALUES (?, ?, ?, ?)", (binary_name, architecture, compiler, compiler_version))
    conn.commit()
    cur.execute("SELECT id FROM binary_name WHERE binary_name = ? ORDER BY id DESC LIMIT 1", (binary_name,))
    binary_name_id = cur.fetchone()[0] 
        

    # id_file = [ id[0] for id  in id_filename.fetchall()]

    for function_name in list_of_function:

        disassambly_function = get_dis_asm_by_function(function_name)
        
        # Commit the transaction
        cur.execute("INSERT INTO function_name (function_name) VALUES (?)", (function_name,))
        conn.commit()
        cur.execute("SELECT id FROM function_name WHERE function_name = ? ORDER BY id DESC LIMIT 1", (function_name,))
        function_id = cur.fetchone()[0]

        cur.execute("INSERT INTO binary_function_mapping (binary_id, function_id) VALUES (?, ?)", (binary_name_id, function_id,))
        conn.commit()

        cur.execute("INSERT INTO function_disassambly (function_id, disassambly) VALUES (?, ?)", (function_id, pickle.dumps(disassambly_function),))
        conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()


    
   


    

    


if __name__ == '__main__':
    if not idaapi.get_plugin_options("file_name"):
        print("[!] -file_name option is missing")
        idc.Exit(1)
    
    plugin_options = idaapi.get_plugin_options("file_name").split("@")
    file_name = plugin_options[0]
    software_list = plugin_options[1]

    main(file_name, software_list)
    idc.Exit(0)
    






