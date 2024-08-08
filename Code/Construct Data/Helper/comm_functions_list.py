import json
import os

list_folders=["clamav", "curl", "nmap", "openssl", "unrar", "zlib"]


save_directory = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\functions"

with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\vocab_function.json") as josn_file:

    data = json.load(josn_file)



def get_commom_function_name(json_path):
    with open(json_path, "r") as json_file:
        data_read = json.load(json_file)
    list_tems = list(data_read.values())
    common_items = set(list_tems [0]).intersection(*list_tems [1:])
    return common_items
    

with open("D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\results\\all_commom_funct.json", "w") as json_file:
    dict_data = {}

    for folder in list_folders:

        dict_data[folder] = {}
        functions = data[folder]
        path_dics = os.path.join(save_directory, folder)
        for funct in functions:
            file_path = os.path.join(path_dics, funct, funct)
            json_path = os.path.join(file_path, file_path + ".json")
            f = get_commom_function_name(json_path)
            dict_data[folder][funct] = list(f)

    json.dump(dict_data, json_file, indent=4)

    
            
    

            



