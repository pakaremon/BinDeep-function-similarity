
import re
import sqlite3
import json

database_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Helper\\Database\\bin_similar.db"

data_path = "D:\\HocTap\\HK2_2023_2024\\ML\\Project\\Dataset\\jsonDataset\\curl\\x64-gcc-9-O1_curl.json"
# D:\HocTap\HK2_2023_2024\ML\Project\Dataset\jsonDataset\curl\x64-gcc-4.8-O1_curl.json

with open(data_path, "r") as json_file:
    data = json.load(json_file)


filenames = 'arm32-clang-3.5-O0_afalg.so'

list_item_binary = filenames.split('-')

binary_name = list_item_binary[-1]
architecture = list_item_binary[0]
compiler = list_item_binary[1]
compiler_version = list_item_binary[2]

print(binary_name)
print(architecture)
print(compiler)
print(compiler_version)


# file_name = "x64-gcc-9-O1_curl.json"
# if matches := re.search(r'^(x86|x64|arm32|arm64).+$', file_name ,re.IGNORECASE):
#     architecture = matches[1]

# function_list = [f for f in data.keys()]


# conn = sqlite3.connect(database_path)
# cur = conn.cursor()

# # cur.execute("SELECT id FROM file_name WHERE file_name = ?", (file_name,))
# # id_filename = cur.fetchone()[0]

# cur.execute("INSERT INTO file_name (file_name, arch) VALUES (?, ?)", (file_name, architecture))
# conn.commit()
# cur.execute("SELECT id FROM file_name WHERE file_name = ?", (file_name,))
# id_filename = cur.fetchone()[0] 
    

# # id_file = [ id[0] for id  in id_filename.fetchall()]

# for function_name in function_list:
    
#     # Commit the transaction
#     cur.execute("INSERT INTO function_name (function_name) VALUES (?)", (function_name,))
#     conn.commit()
#     cur.execute("SELECT id FROM function_name WHERE function_name = ? ORDER BY id DESC LIMIT 1", (function_name,))
#     id_function = cur.fetchone()[0]

#     cur.execute("INSERT INTO file_function_mapping (file_id, function_id) VALUES (?, ?)", (id_filename, id_function))
#     conn.commit()

#     cur.execute("INSERT INTO function_disassambly (function_id, disassambly) VALUES (?, ?)", (id_function, json.dumps(data[function_name])))
#     conn.commit()

# # Close the cursor and connection
# cur.close()
# conn.close()

