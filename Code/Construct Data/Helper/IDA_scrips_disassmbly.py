
import idaapi

import idautils
import idc
import json
import pickle
import os
from  os.path import isfile 

# from collections import namedtuple




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



dict_results = {}

def get_bitness():
    """Return 32/64 according to the binary bitness."""
    info = idaapi.get_inf_structure()
    if info.is_64bit():
        return 64
    elif info.is_32bit():
        return 32




def convert_procname_to_str(procname, bitness):
    """Convert the arch and bitness to a std. format."""
    if procname == 'mipsb':
        return "mips-{}".format(bitness)
    if procname == "arm":
        return "arm-{}".format(bitness)
    if "pc" in procname:
        return "x86-{}".format(bitness)
    raise RuntimeError(
        "[!] Arch not supported ({}, {})".format(
            procname, bitness))



def get_dis_asm_by_function(fuction_name):
    list_of_instructions = []
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

    dict_results[fuction_name] = list_of_instructions

def main(file_name, file_path ):
    # bitness = get_bitness()
    # procname = idaapi.get_inf_structure().procName.lower()
   
    # dict_results['arch'] = convert_procname_to_str(procname, bitness)

    # for fuction_name in list_of_function:
    #     get_dis_asm_by_function(fuction_name)
    

    print(file_name)
    print(real_names)
    data = {}
    json_file_name = file_path + "\\" + os.path.basename(file_path) + ".json"
    if not isfile(json_file_name):
        with open(json_file_name, "w") as json_file:
            json.dump({}, json_file, indent=4)
    


    with open(json_file_name , "r") as file_json:
        data = json.load(file_json)


    data[file_name] = real_names
    with open(json_file_name , "w") as file_json:
        json.dump(data, file_json, indent=4)




    # print(dict_results)

    # with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\jsonDataset\\curl\\arm32-clang-3.5-O1_curl.json", 'w') as file_json:
    #     json.dump(dict_results, file_json, indent=4)

    # print("===end of program")

if __name__=='__main__':
    if not idaapi.get_plugin_options("file_name"):
        print("[!] -file_name option is missing")
        idc.Exit(1)
    
    plugin_options = idaapi.get_plugin_options("file_name").split("@")
    file_name = plugin_options[0]
    file_path = plugin_options[1]

    main(file_name, file_path)
    idc.Exit(0)
    